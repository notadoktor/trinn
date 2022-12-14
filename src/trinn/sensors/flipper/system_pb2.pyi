"""
This file was auto-generated by gen_stubs.py
"""

from __future__ import annotations

from enum import IntEnum
from typing import Literal

import google.protobuf.descriptor
import google.protobuf.message
import google.protobuf.symbol_database

import trinn.sensors.flipper.system_pb2

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor
_sym_db: google.protobuf.symbol_database.SymbolDatabase

class PingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: int
    data: bytes
    def __init__(self, *, data: bytes = ...) -> None: ...
    def ClearField(self, field_name: Literal["data"]) -> None: ...

class PingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: int
    data: bytes
    def __init__(self, *, data: bytes = ...) -> None: ...
    def ClearField(self, field_name: Literal["data"]) -> None: ...

class RebootRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODE_FIELD_NUMBER: int
    mode: RebootMode
    def __init__(self, *, mode: RebootMode = ...) -> None: ...
    def ClearField(self, field_name: Literal["mode"]) -> None: ...

class DeviceInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class DeviceInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: int
    VALUE_FIELD_NUMBER: int
    key: str
    value: str
    def __init__(self, *, key: str = ..., value: str = ...) -> None: ...
    def ClearField(self, field_name: Literal["key", "value"]) -> None: ...

class FactoryResetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class GetDateTimeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class GetDateTimeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATETIME_FIELD_NUMBER: int
    datetime: trinn.sensors.flipper.system_pb2.DateTime
    def __init__(self, *, datetime: trinn.sensors.flipper.system_pb2.DateTime = ...) -> None: ...
    def ClearField(self, field_name: Literal["datetime"]) -> None: ...

class SetDateTimeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATETIME_FIELD_NUMBER: int
    datetime: trinn.sensors.flipper.system_pb2.DateTime
    def __init__(self, *, datetime: trinn.sensors.flipper.system_pb2.DateTime = ...) -> None: ...
    def ClearField(self, field_name: Literal["datetime"]) -> None: ...

class DateTime(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    HOUR_FIELD_NUMBER: int
    MINUTE_FIELD_NUMBER: int
    SECOND_FIELD_NUMBER: int
    DAY_FIELD_NUMBER: int
    MONTH_FIELD_NUMBER: int
    YEAR_FIELD_NUMBER: int
    WEEKDAY_FIELD_NUMBER: int
    hour: int
    minute: int
    second: int
    day: int
    month: int
    year: int
    weekday: int
    def __init__(
        self,
        *,
        hour: int = ...,
        minute: int = ...,
        second: int = ...,
        day: int = ...,
        month: int = ...,
        year: int = ...,
        weekday: int = ...,
    ) -> None: ...
    def ClearField(
        self, field_name: Literal["hour", "minute", "second", "day", "month", "year", "weekday"]
    ) -> None: ...

class PlayAudiovisualAlertRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class ProtobufVersionRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class ProtobufVersionResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MAJOR_FIELD_NUMBER: int
    MINOR_FIELD_NUMBER: int
    major: int
    minor: int
    def __init__(self, *, major: int = ..., minor: int = ...) -> None: ...
    def ClearField(self, field_name: Literal["major", "minor"]) -> None: ...

class UpdateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UPDATE_MANIFEST_FIELD_NUMBER: int
    update_manifest: str
    def __init__(self, *, update_manifest: str = ...) -> None: ...
    def ClearField(self, field_name: Literal["update_manifest"]) -> None: ...

class UpdateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: int
    code: UpdateResultCode
    def __init__(self, *, code: UpdateResultCode = ...) -> None: ...
    def ClearField(self, field_name: Literal["code"]) -> None: ...

class PowerInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class PowerInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: int
    VALUE_FIELD_NUMBER: int
    key: str
    value: str
    def __init__(self, *, key: str = ..., value: str = ...) -> None: ...
    def ClearField(self, field_name: Literal["key", "value"]) -> None: ...

class RebootMode(IntEnum):
    OS = 0
    DFU = 1
    UPDATE = 2

OS = RebootMode.OS
DFU = RebootMode.DFU
UPDATE = RebootMode.UPDATE

class UpdateResultCode(IntEnum):
    OK = 0
    ManifestPathInvalid = 1
    ManifestFolderNotFound = 2
    ManifestInvalid = 3
    StageMissing = 4
    StageIntegrityError = 5
    ManifestPointerError = 6
    TargetMismatch = 7
    OutdatedManifestVersion = 8
    IntFull = 9
    UnspecifiedError = 10

OK = UpdateResultCode.OK
ManifestPathInvalid = UpdateResultCode.ManifestPathInvalid
ManifestFolderNotFound = UpdateResultCode.ManifestFolderNotFound
ManifestInvalid = UpdateResultCode.ManifestInvalid
StageMissing = UpdateResultCode.StageMissing
StageIntegrityError = UpdateResultCode.StageIntegrityError
ManifestPointerError = UpdateResultCode.ManifestPointerError
TargetMismatch = UpdateResultCode.TargetMismatch
OutdatedManifestVersion = UpdateResultCode.OutdatedManifestVersion
IntFull = UpdateResultCode.IntFull
UnspecifiedError = UpdateResultCode.UnspecifiedError
