#!/usr/bin/env python3

from pathlib import Path
from typing import ClassVar, overload

from google.protobuf.internal.encoder import _VarintBytes  # type: ignore
from google.protobuf.message import Message
from serial import Serial

from ..generic import GenericClient
from . import application_pb2, flipper_pb2, gpio_pb2, gui_pb2, storage_pb2, system_pb2


class Varint32Exception(Exception):
    pass


class Client(GenericClient):
    is_open: bool = False
    _type: ClassVar[str] = "flipperzero"

    def __init__(self, dev: str, baudrate: int = 230400, *, lazy_connect: bool = False):
        if not Path(dev).exists():
            raise FileNotFoundError(f"Device {dev} not found")

        self._serial = Serial(dev, baudrate=baudrate, timeout=1)
        self._cmd_id = 0

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
        # cmd_obj = _get_symbol(cmd)
        # breakpoint()
        cmd_data = _get_symbol(cmd)(**kwargs)
        msg = self._new_msg(
            command_id=self._next_cmd_id(),
            has_next=has_next,
            command_status=flipper_pb2.CommandStatus.OK,
            **{cmd: cmd_data},
        )
        msg_bytes = bytearray(_VarintBytes(msg.ByteSize()) + msg.SerializeToString())
        self._serial.write(msg_bytes)
        if get_response:
            return self._read_answer(0)

    def _new_msg(self, **kwargs):
        return flipper_pb2.Main(**kwargs)

    ### Application commands

    def ping(self, data=bytes([0xDE, 0xAD, 0xBE, 0xEF])):
        """Ping flipper"""
        return self._run("system_ping_request", get_response=True, data=data)

    def start_screen_stream(self, get_resp: bool = True):
        """Start screen stream"""
        return self._run("gui_start_screen_stream_request", get_response=get_resp)

    def stop_screen_stream(self, get_resp: bool = False):
        """Stop screen stream"""
        return self._run("gui_stop_screen_stream_request", get_response=get_resp)

    def snapshot_screen(self):
        """Snapshot screen"""
        data = self.start_screen_stream()
        self.stop_screen_stream()
        return data.gui_screen_frame.data

    def _send_input_event_request(
        self,
        input_key: gui_pb2.InputKey,
        input_type: gui_pb2.InputType,
        *,
        get_resp: bool = False,
    ):
        """Send Input Event Request Key"""
        return self._run(
            "gui_send_input_event_request",
            get_response=get_resp,
            key=input_key,
            type=input_type,
        )

    def send_input(self, key_type: str):
        """Send Input Event Request Type"""
        input_type_str, input_key_str = key_type.split(" ")

        try:
            input_type = getattr(gui_pb2.InputType, input_type_str)
        except ValueError:
            raise ValueError(f"Unknown input type: {input_type_str}")

        try:
            input_key = getattr(gui_pb2.InputKey, input_key_str)
        except ValueError:
            raise ValueError(f"Unknown input key: {input_key_str}")

        self._send_input_event_request(input_key, gui_pb2.PRESS)
        self._send_input_event_request(input_key, input_type)
        self._send_input_event_request(input_key, gui_pb2.RELEASE)

    def set_pin_mode(self, pin: gpio_pb2.GpioPin, mode: gpio_pb2.GpioPinMode):
        """Set GPIO pin mode"""
        return self._run("gpio_set_pin_mode_request", get_response=True, pin=pin, mode=mode)

    def write_pin(self, pin: gpio_pb2.GpioPin, value: int):
        """Write GPIO pin"""
        return self._run("gpio_write_pin_request", get_response=True, pin=pin, value=value)

    def read_pin(self, pin: gpio_pb2.GpioPin):
        """Read GPIO pin"""
        return self._run("gpio_read_pin_request", get_response=True, pin=pin)

    def set_input_pull(self, pin: gpio_pb2.GpioPin, pull_mode: gpio_pb2.GpioInputPull):
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


def _get_symbol(name: str) -> type[Message]:
    msg = flipper_pb2.Main.DESCRIPTOR.fields_by_name[name].message_type
    pkg, name = msg.full_name.split(".", 1)
    mod_name = pkg.split("_", 1)[-1].lower() + "_pb2"
    return getattr(globals()[mod_name], name)
