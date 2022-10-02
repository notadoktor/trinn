#!/usr/bin/env python3

from pathlib import Path
from typing import ClassVar, overload

from google.protobuf.internal.encoder import _VarintBytes  # type: ignore
from google.protobuf.symbol_database import SymbolDatabase
from serial import Serial

from ..generic import GenericClient
from . import flipper_pb2, gpio_pb2, gui_pb2, storage_pb2, system_pb2

db = SymbolDatabase()
db.RegisterFileDescriptor(flipper_pb2.DESCRIPTOR)
db.RegisterFileDescriptor(gpio_pb2.DESCRIPTOR)
db.RegisterFileDescriptor(gui_pb2.DESCRIPTOR)
db.RegisterFileDescriptor(storage_pb2.DESCRIPTOR)
db.RegisterFileDescriptor(system_pb2.DESCRIPTOR)


class Varint32Exception(Exception):
    pass


class Client(GenericClient):
    is_open: bool = False
    _type: ClassVar[str] = "flipperzero"

    def __init__(self, dev: str, baudrate: int = 230400, *, lazy_connect: bool = False):
        if not Path(dev).exists():
            raise FileNotFoundError(f"Device {dev} not found")

        self._serial = Serial(dev, baudrate=baudrate, timeout=1)
        self._cmd_id: int = 0

        if not lazy_connect:
            self.connect()

    def _str_info(self):
        return f" cmd={self._cmd_id}"

    def _next_cmd_id(self):
        self._cmd_id += 1
        return self._cmd_id

    def _read_varint_32(self):
        """Read varint from serial port"""
        MASK = (1 << 32) - 1

        result = 0
        shift = 0
        while 1:
            b = int.from_bytes(self._serial.read(size=1), byteorder="little", signed=False)
            result |= (b & 0x7F) << shift
            if not (b & 0x80):
                result &= MASK
                result = int(result)
                return result
            shift += 7
            if shift >= 64:
                raise Varint32Exception("Too many bytes when decoding varint.")
        raise Varint32Exception("Too many bytes when decoding varint.")

    def _read_answer(self, command_id: int | None = None):
        """Read answer from serial port and filter by command id"""
        if command_id == None:
            command_id = self._cmd_id

        while True:
            data = self._read_any()
            if data.command_id == command_id:
                break
        return data

    def _read_any(self):
        """Read answer from serial port"""
        length = self._read_varint_32()
        data = flipper_pb2.Main()
        data.ParseFromString(self._serial.read(size=length))
        return data

    def connect(self):
        if self.is_open:
            return

        self._serial.flushOutput()
        self._serial.flushInput()
        self._serial.timeout = None

        # wait for prompt
        self._serial.read_until(b">: ")

        # send command and skip answer
        self._serial.write(b"start_rpc_session\r")
        self._serial.read_until(b"\n")
        self.is_open = True

    @overload
    def _run(
        self, cmd: str, *, has_next: bool = False, get_response: bool = True, **kwargs
    ) -> flipper_pb2.Main:
        ...

    @overload
    def _run(
        self, cmd: str, *, has_next: bool = False, get_response: bool = False, **kwargs
    ) -> None:
        ...

    def _run(self, cmd: str, *, has_next: bool = False, get_response: bool = False, **kwargs):
        cmd_data = db.GetSymbol("cmd")(**kwargs)
        msg = db.GetSymbol("Main")(
            command_id=self._next_cmd_id(),
            has_next=has_next,
            command_status=flipper_pb2.CommandStatus("OK"),
            cmd=cmd_data,
        )
        msg_bytes = bytearray(_VarintBytes(msg.ByteSize()) + msg.SerializeToString())
        self._serial.write(msg_bytes)
        if get_response:
            return self._read_answer(self._cmd_id)

    def ping(self, data=bytes([0xDE, 0xAD, 0xBE, 0xEF])):
        """Ping flipper"""
        return self._run("system_ping_request", get_response=True, data=data)

    def start_screen_stream(self, get_resp: bool = True):
        """Start screen stream"""
        return self._run("gui_start_screen_stream_request", get_response=get_resp)

    def stop_screen_stream(self, get_resp: bool = True):
        """Stop screen stream"""
        return self._run("gui_stop_screen_stream_request")

    def snapshot_screen(self):
        """Snapshot screen"""
        data = self.start_screen_stream()
        self.stop_screen_stream(False)
        return data.gui_screen_frame  # data.gui_screen_frame.data

    def _send_input_event_request(
        self,
        input_key: gui_pb2.InputKey,
        input_type: gui_pb2.InputType,
    ):
        """Send Input Event Request Key"""
        return self._run(
            "gui_send_input_event_request",
            get_response=True,
            key=input_key,
            type=input_type,
        )

    def send_input(self, key_type: str):
        """Send Input Event Request Type"""
        input_type_str, input_key_str = key_type.split(" ")

        try:
            input_type = gui_pb2.InputType(input_type_str)
        except ValueError:
            raise ValueError(f"Unknown input type: {input_type_str}")

        try:
            input_key = gui_pb2.InputKey(input_key_str)
        except ValueError:
            raise ValueError(f"Unknown input key: {input_key_str}")

        self._send_input_event_request(input_key, gui_pb2.PRESS)
        self._send_input_event_request(input_key, input_type)
        self._send_input_event_request(input_key, gui_pb2.RELEASE)

    def app_start(self, name, args):
        """Start application"""
        return self._run("app_start_request", get_response=True, name=name, args=args)

    def app_exit(self):
        """Send exit command to app"""
        return self._run("app_exit_request", get_response=True)

    def app_load_file(self, path):
        """Send load file command to app"""
        return self._run("app_load_file_request", get_response=True, path=path)

    def app_button_press(self, args):
        """Send button press command to app"""
        return self._run("app_button_press_request", get_response=True, args=args)

    def app_button_release(self):
        """Send button release command to app"""
        return self._run("app_button_release_request", get_response=True)

    def cmd_flipper_stop_session(self):
        """Stop RPC session"""
        return self._run("stop_session", get_response=True)

    def gpio_set_pin_mode(self, pin, mode):
        """Set GPIO pin mode"""
        return self._run("gpio_set_pin_mode_request", get_response=True, pin=pin, mode=mode)

    def cmd_gpio_write_pin(self, pin, value):
        """Write GPIO pin"""
        return self._run("gpio_write_pin_request", get_response=True, pin=pin, value=value)

    def cmd_gpio_read_pin(self, pin):
        """Read GPIO pin"""
        return self._run("gpio_read_pin_request", get_response=True, pin=pin)

    def cmd_gpio_set_input_pull(self, pin, pull_mode):
        """Set GPIO input pull"""
        return self._run(
            "gpio_set_input_pull_request",
            get_response=True,
            pin=pin,
            pull_mode=pull_mode,
        )

    def read(self, size=1):
        pass

    def poll(self, interval):
        pass
