"""
This file was auto-generated by gen_stubs.py
"""

from __future__ import annotations

from enum import IntEnum
from typing import Literal

import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.symbol_database

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
_sym_db: google.protobuf.symbol_database.SymbolDatabase

class SetPinMode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    MODE_FIELD_NUMBER: int
    pin: GpioPin
    mode: GpioPinMode
    def __init__(self, *, pin: GpioPin = ..., mode: GpioPinMode = ...) -> None: ...
    def ClearField(self, field_name: Literal["pin", "mode"]) -> None: ...

class SetInputPull(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    PULL_MODE_FIELD_NUMBER: int
    pin: GpioPin
    pull_mode: GpioInputPull
    def __init__(self, *, pin: GpioPin = ..., pull_mode: GpioInputPull = ...) -> None: ...
    def ClearField(self, field_name: Literal["pin", "pull_mode"]) -> None: ...

class GetPinMode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    pin: GpioPin
    def __init__(self, *, pin: GpioPin = ...) -> None: ...
    def ClearField(self, field_name: Literal["pin"]) -> None: ...

class GetPinModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODE_FIELD_NUMBER: int
    mode: GpioPinMode
    def __init__(self, *, mode: GpioPinMode = ...) -> None: ...
    def ClearField(self, field_name: Literal["mode"]) -> None: ...

class ReadPin(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    pin: GpioPin
    def __init__(self, *, pin: GpioPin = ...) -> None: ...
    def ClearField(self, field_name: Literal["pin"]) -> None: ...

class ReadPinResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: int
    value: int
    def __init__(self, *, value: int = ...) -> None: ...
    def ClearField(self, field_name: Literal["value"]) -> None: ...

class WritePin(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    VALUE_FIELD_NUMBER: int
    pin: GpioPin
    value: int
    def __init__(self, *, pin: GpioPin = ..., value: int = ...) -> None: ...
    def ClearField(self, field_name: Literal["pin", "value"]) -> None: ...

class GpioPin(IntEnum):
    PC0 = 0
    PC1 = 1
    PC3 = 2
    PB2 = 3
    PB3 = 4
    PA4 = 5
    PA6 = 6
    PA7 = 7

PC0 = GpioPin.PC0
PC1 = GpioPin.PC1
PC3 = GpioPin.PC3
PB2 = GpioPin.PB2
PB3 = GpioPin.PB3
PA4 = GpioPin.PA4
PA6 = GpioPin.PA6
PA7 = GpioPin.PA7

class GpioPinMode(IntEnum):
    OUTPUT = 0
    INPUT = 1

OUTPUT = GpioPinMode.OUTPUT
INPUT = GpioPinMode.INPUT

class GpioInputPull(IntEnum):
    NO = 0
    UP = 1
    DOWN = 2

NO = GpioInputPull.NO
UP = GpioInputPull.UP
DOWN = GpioInputPull.DOWN
