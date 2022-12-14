"""
This file was auto-generated by gen_helpers.py at 2022-09-30T13:14
"""

from __future__ import annotations

from typing import TYPE_CHECKING, Literal

import google.protobuf.descriptor
import google.protobuf.message

from . import flipper_pb2, gui_pb2, system_pb2, storage_pb2, gpio_pb2, application_pb2
if TYPE_CHECKING:
    from .client import Client
else:
    from ..generic import GenericClient as Client

class MetaHelper:
    def __init__(self, name: str, client: Client):
        self._name = name
        self._client = client

    def run(self, cmd: str, *args, **kwargs):
        try:
            cmd_obj = getattr(self, cmd)
        except AttributeError:
            raise SyntaxError(f"Unknown command {cmd}")

        return cmd_obj(*args, **kwargs)

class Flipper(MetaHelper):

    def __init__(self, client: Client):
        super().__init__("flipper", client)

class Empty(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class StopSession(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class Main(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COMMAND_ID_FIELD_NUMBER: int
    COMMAND_STATUS_FIELD_NUMBER: int
    HAS_NEXT_FIELD_NUMBER: int
    EMPTY_FIELD_NUMBER: int
    STOP_SESSION_FIELD_NUMBER: int
    SYSTEM_PING_REQUEST_FIELD_NUMBER: int
    SYSTEM_PING_RESPONSE_FIELD_NUMBER: int
    SYSTEM_REBOOT_REQUEST_FIELD_NUMBER: int
    SYSTEM_DEVICE_INFO_REQUEST_FIELD_NUMBER: int
    SYSTEM_DEVICE_INFO_RESPONSE_FIELD_NUMBER: int
    SYSTEM_FACTORY_RESET_REQUEST_FIELD_NUMBER: int
    SYSTEM_GET_DATETIME_REQUEST_FIELD_NUMBER: int
    SYSTEM_GET_DATETIME_RESPONSE_FIELD_NUMBER: int
    SYSTEM_SET_DATETIME_REQUEST_FIELD_NUMBER: int
    SYSTEM_PLAY_AUDIOVISUAL_ALERT_REQUEST_FIELD_NUMBER: int
    SYSTEM_PROTOBUF_VERSION_REQUEST_FIELD_NUMBER: int
    SYSTEM_PROTOBUF_VERSION_RESPONSE_FIELD_NUMBER: int
    SYSTEM_UPDATE_REQUEST_FIELD_NUMBER: int
    SYSTEM_UPDATE_RESPONSE_FIELD_NUMBER: int
    SYSTEM_POWER_INFO_REQUEST_FIELD_NUMBER: int
    SYSTEM_POWER_INFO_RESPONSE_FIELD_NUMBER: int
    STORAGE_INFO_REQUEST_FIELD_NUMBER: int
    STORAGE_INFO_RESPONSE_FIELD_NUMBER: int
    STORAGE_STAT_REQUEST_FIELD_NUMBER: int
    STORAGE_STAT_RESPONSE_FIELD_NUMBER: int
    STORAGE_LIST_REQUEST_FIELD_NUMBER: int
    STORAGE_LIST_RESPONSE_FIELD_NUMBER: int
    STORAGE_READ_REQUEST_FIELD_NUMBER: int
    STORAGE_READ_RESPONSE_FIELD_NUMBER: int
    STORAGE_WRITE_REQUEST_FIELD_NUMBER: int
    STORAGE_DELETE_REQUEST_FIELD_NUMBER: int
    STORAGE_MKDIR_REQUEST_FIELD_NUMBER: int
    STORAGE_MD5SUM_REQUEST_FIELD_NUMBER: int
    STORAGE_MD5SUM_RESPONSE_FIELD_NUMBER: int
    STORAGE_RENAME_REQUEST_FIELD_NUMBER: int
    STORAGE_BACKUP_CREATE_REQUEST_FIELD_NUMBER: int
    STORAGE_BACKUP_RESTORE_REQUEST_FIELD_NUMBER: int
    APP_START_REQUEST_FIELD_NUMBER: int
    APP_LOCK_STATUS_REQUEST_FIELD_NUMBER: int
    APP_LOCK_STATUS_RESPONSE_FIELD_NUMBER: int
    APP_EXIT_REQUEST_FIELD_NUMBER: int
    APP_LOAD_FILE_REQUEST_FIELD_NUMBER: int
    APP_BUTTON_PRESS_REQUEST_FIELD_NUMBER: int
    APP_BUTTON_RELEASE_REQUEST_FIELD_NUMBER: int
    GUI_START_SCREEN_STREAM_REQUEST_FIELD_NUMBER: int
    GUI_STOP_SCREEN_STREAM_REQUEST_FIELD_NUMBER: int
    GUI_SCREEN_FRAME_FIELD_NUMBER: int
    GUI_SEND_INPUT_EVENT_REQUEST_FIELD_NUMBER: int
    GUI_START_VIRTUAL_DISPLAY_REQUEST_FIELD_NUMBER: int
    GUI_STOP_VIRTUAL_DISPLAY_REQUEST_FIELD_NUMBER: int
    GPIO_SET_PIN_MODE_FIELD_NUMBER: int
    GPIO_SET_INPUT_PULL_FIELD_NUMBER: int
    GPIO_GET_PIN_MODE_FIELD_NUMBER: int
    GPIO_GET_PIN_MODE_RESPONSE_FIELD_NUMBER: int
    GPIO_READ_PIN_FIELD_NUMBER: int
    GPIO_READ_PIN_RESPONSE_FIELD_NUMBER: int
    GPIO_WRITE_PIN_FIELD_NUMBER: int
    APP_STATE_RESPONSE_FIELD_NUMBER: int
    command_id: int
    command_status: CommandStatus
    has_next: bool
    empty: int
    stop_session: int
    system_ping_request: int
    system_ping_response: int
    system_reboot_request: int
    system_device_info_request: int
    system_device_info_response: int
    system_factory_reset_request: int
    system_get_datetime_request: int
    system_get_datetime_response: int
    system_set_datetime_request: int
    system_play_audiovisual_alert_request: int
    system_protobuf_version_request: int
    system_protobuf_version_response: int
    system_update_request: int
    system_update_response: int
    system_power_info_request: int
    system_power_info_response: int
    storage_info_request: int
    storage_info_response: int
    storage_stat_request: int
    storage_stat_response: int
    storage_list_request: int
    storage_list_response: int
    storage_read_request: int
    storage_read_response: int
    storage_write_request: int
    storage_delete_request: int
    storage_mkdir_request: int
    storage_md5sum_request: int
    storage_md5sum_response: int
    storage_rename_request: int
    storage_backup_create_request: int
    storage_backup_restore_request: int
    app_start_request: int
    app_lock_status_request: int
    app_lock_status_response: int
    app_exit_request: int
    app_load_file_request: int
    app_button_press_request: int
    app_button_release_request: int
    gui_start_screen_stream_request: int
    gui_stop_screen_stream_request: int
    gui_screen_frame: int
    gui_send_input_event_request: int
    gui_start_virtual_display_request: int
    gui_stop_virtual_display_request: int
    gpio_set_pin_mode: int
    gpio_set_input_pull: int
    gpio_get_pin_mode: int
    gpio_get_pin_mode_response: int
    gpio_read_pin: int
    gpio_read_pin_response: int
    gpio_write_pin: int
    app_state_response: int
    def __init__(self, *, command_id: int=..., command_status: CommandStatus=..., has_next: bool=..., empty: int=..., stop_session: int=..., system_ping_request: int=..., system_ping_response: int=..., system_reboot_request: int=..., system_device_info_request: int=..., system_device_info_response: int=..., system_factory_reset_request: int=..., system_get_datetime_request: int=..., system_get_datetime_response: int=..., system_set_datetime_request: int=..., system_play_audiovisual_alert_request: int=..., system_protobuf_version_request: int=..., system_protobuf_version_response: int=..., system_update_request: int=..., system_update_response: int=..., system_power_info_request: int=..., system_power_info_response: int=..., storage_info_request: int=..., storage_info_response: int=..., storage_stat_request: int=..., storage_stat_response: int=..., storage_list_request: int=..., storage_list_response: int=..., storage_read_request: int=..., storage_read_response: int=..., storage_write_request: int=..., storage_delete_request: int=..., storage_mkdir_request: int=..., storage_md5sum_request: int=..., storage_md5sum_response: int=..., storage_rename_request: int=..., storage_backup_create_request: int=..., storage_backup_restore_request: int=..., app_start_request: int=..., app_lock_status_request: int=..., app_lock_status_response: int=..., app_exit_request: int=..., app_load_file_request: int=..., app_button_press_request: int=..., app_button_release_request: int=..., gui_start_screen_stream_request: int=..., gui_stop_screen_stream_request: int=..., gui_screen_frame: int=..., gui_send_input_event_request: int=..., gui_start_virtual_display_request: int=..., gui_stop_virtual_display_request: int=..., gpio_set_pin_mode: int=..., gpio_set_input_pull: int=..., gpio_get_pin_mode: int=..., gpio_get_pin_mode_response: int=..., gpio_read_pin: int=..., gpio_read_pin_response: int=..., gpio_write_pin: int=..., app_state_response: int=...) -> None: ...

    def ClearField(self, field_name: Literal['command_id', 'command_status', 'has_next', 'empty', 'stop_session', 'system_ping_request', 'system_ping_response', 'system_reboot_request', 'system_device_info_request', 'system_device_info_response', 'system_factory_reset_request', 'system_get_datetime_request', 'system_get_datetime_response', 'system_set_datetime_request', 'system_play_audiovisual_alert_request', 'system_protobuf_version_request', 'system_protobuf_version_response', 'system_update_request', 'system_update_response', 'system_power_info_request', 'system_power_info_response', 'storage_info_request', 'storage_info_response', 'storage_stat_request', 'storage_stat_response', 'storage_list_request', 'storage_list_response', 'storage_read_request', 'storage_read_response', 'storage_write_request', 'storage_delete_request', 'storage_mkdir_request', 'storage_md5sum_request', 'storage_md5sum_response', 'storage_rename_request', 'storage_backup_create_request', 'storage_backup_restore_request', 'app_start_request', 'app_lock_status_request', 'app_lock_status_response', 'app_exit_request', 'app_load_file_request', 'app_button_press_request', 'app_button_release_request', 'gui_start_screen_stream_request', 'gui_stop_screen_stream_request', 'gui_screen_frame', 'gui_send_input_event_request', 'gui_start_virtual_display_request', 'gui_stop_virtual_display_request', 'gpio_set_pin_mode', 'gpio_set_input_pull', 'gpio_get_pin_mode', 'gpio_get_pin_mode_response', 'gpio_read_pin', 'gpio_read_pin_response', 'gpio_write_pin', 'app_state_response']) -> None: ...

class Region(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    COUNTRY_CODE_FIELD_NUMBER: int
    BANDS_FIELD_NUMBER: int
    country_code: str
    bands: int
    def __init__(self, *, country_code: str=..., bands: int=...) -> None: ...

    def ClearField(self, field_name: Literal['country_code', 'bands']) -> None: ...

class Band(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    START_FIELD_NUMBER: int
    END_FIELD_NUMBER: int
    POWER_LIMIT_FIELD_NUMBER: int
    DUTY_CYCLE_FIELD_NUMBER: int
    start: int
    end: int
    power_limit: int
    duty_cycle: int
    def __init__(self, *, start: int=..., end: int=..., power_limit: int=..., duty_cycle: int=...) -> None: ...

    def ClearField(self, field_name: Literal['start', 'end', 'power_limit', 'duty_cycle']) -> None: ...


    class enums:
        MetaEnum(name='CommandStatus', values={'OK': 0, 'ERROR': 1, 'ERROR_DECODE': 2, 'ERROR_NOT_IMPLEMENTED': 3, 'ERROR_BUSY': 4, 'ERROR_CONTINUOUS_COMMAND_INTERRUPTED': 14, 'ERROR_INVALID_PARAMETERS': 15, 'ERROR_STORAGE_NOT_READY': 5, 'ERROR_STORAGE_EXIST': 6, 'ERROR_STORAGE_NOT_EXIST': 7, 'ERROR_STORAGE_INVALID_PARAMETER': 8, 'ERROR_STORAGE_DENIED': 9, 'ERROR_STORAGE_INVALID_NAME': 10, 'ERROR_STORAGE_INTERNAL': 11, 'ERROR_STORAGE_NOT_IMPLEMENTED': 12, 'ERROR_STORAGE_ALREADY_OPEN': 13, 'ERROR_STORAGE_DIR_NOT_EMPTY': 18, 'ERROR_APP_CANT_START': 16, 'ERROR_APP_SYSTEM_LOCKED': 17, 'ERROR_APP_NOT_RUNNING': 21, 'ERROR_APP_CMD_ERROR': 22, 'ERROR_VIRTUAL_DISPLAY_ALREADY_STARTED': 19, 'ERROR_VIRTUAL_DISPLAY_NOT_STARTED': 20, 'ERROR_GPIO_MODE_INCORRECT': 58, 'ERROR_GPIO_UNKNOWN_PIN_MODE': 59})

class Gui(MetaHelper):

    def __init__(self, client: Client):
        super().__init__("gui", client)

class ScreenFrame(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: int
    data: str
    def __init__(self, *, data: str=...) -> None: ...

    def ClearField(self, field_name: Literal['data']) -> None: ...

class StartScreenStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class StopScreenStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class SendInputEventRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: int
    TYPE_FIELD_NUMBER: int
    key: InputKey
    type: InputType
    def __init__(self, *, key: InputKey=..., type: InputType=...) -> None: ...

    def ClearField(self, field_name: Literal['key', 'type']) -> None: ...

class StartVirtualDisplayRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FIRST_FRAME_FIELD_NUMBER: int
    first_frame: int
    def __init__(self, *, first_frame: int=...) -> None: ...

    def ClearField(self, field_name: Literal['first_frame']) -> None: ...

class StopVirtualDisplayRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...


    class enums:
        MetaEnum(name='InputKey', values={'UP': 0, 'DOWN': 1, 'RIGHT': 2, 'LEFT': 3, 'OK': 4, 'BACK': 5})
        MetaEnum(name='InputType', values={'PRESS': 0, 'RELEASE': 1, 'SHORT': 2, 'LONG': 3, 'REPEAT': 4})

class System(MetaHelper):

    def __init__(self, client: Client):
        super().__init__("system", client)

class PingRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: int
    data: str
    def __init__(self, *, data: str=...) -> None: ...

    def ClearField(self, field_name: Literal['data']) -> None: ...

class PingResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATA_FIELD_NUMBER: int
    data: str
    def __init__(self, *, data: str=...) -> None: ...

    def ClearField(self, field_name: Literal['data']) -> None: ...

class RebootRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODE_FIELD_NUMBER: int
    mode: RebootMode
    def __init__(self, *, mode: RebootMode=...) -> None: ...

    def ClearField(self, field_name: Literal['mode']) -> None: ...

class DeviceInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class DeviceInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: int
    VALUE_FIELD_NUMBER: int
    key: str
    value: str
    def __init__(self, *, key: str=..., value: str=...) -> None: ...

    def ClearField(self, field_name: Literal['key', 'value']) -> None: ...

class FactoryResetRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class GetDateTimeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class GetDateTimeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATETIME_FIELD_NUMBER: int
    datetime: int
    def __init__(self, *, datetime: int=...) -> None: ...

    def ClearField(self, field_name: Literal['datetime']) -> None: ...

class SetDateTimeRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    DATETIME_FIELD_NUMBER: int
    datetime: int
    def __init__(self, *, datetime: int=...) -> None: ...

    def ClearField(self, field_name: Literal['datetime']) -> None: ...

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
    def __init__(self, *, hour: int=..., minute: int=..., second: int=..., day: int=..., month: int=..., year: int=..., weekday: int=...) -> None: ...

    def ClearField(self, field_name: Literal['hour', 'minute', 'second', 'day', 'month', 'year', 'weekday']) -> None: ...

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
    def __init__(self, *, major: int=..., minor: int=...) -> None: ...

    def ClearField(self, field_name: Literal['major', 'minor']) -> None: ...

class UpdateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    UPDATE_MANIFEST_FIELD_NUMBER: int
    update_manifest: str
    def __init__(self, *, update_manifest: str=...) -> None: ...

    def ClearField(self, field_name: Literal['update_manifest']) -> None: ...

class UpdateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    CODE_FIELD_NUMBER: int
    code: UpdateResultCode
    def __init__(self, *, code: UpdateResultCode=...) -> None: ...

    def ClearField(self, field_name: Literal['code']) -> None: ...

class PowerInfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class PowerInfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    KEY_FIELD_NUMBER: int
    VALUE_FIELD_NUMBER: int
    key: str
    value: str
    def __init__(self, *, key: str=..., value: str=...) -> None: ...

    def ClearField(self, field_name: Literal['key', 'value']) -> None: ...


    class enums:
        MetaEnum(name='RebootMode', values={'OS': 0, 'DFU': 1, 'UPDATE': 2})
        MetaEnum(name='UpdateResultCode', values={'OK': 0, 'ManifestPathInvalid': 1, 'ManifestFolderNotFound': 2, 'ManifestInvalid': 3, 'StageMissing': 4, 'StageIntegrityError': 5, 'ManifestPointerError': 6, 'TargetMismatch': 7, 'OutdatedManifestVersion': 8, 'IntFull': 9, 'UnspecifiedError': 10})

class Storage(MetaHelper):

    def __init__(self, client: Client):
        super().__init__("storage", client)

class File(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TYPE_FIELD_NUMBER: int
    NAME_FIELD_NUMBER: int
    SIZE_FIELD_NUMBER: int
    DATA_FIELD_NUMBER: int
    type: FileType
    name: str
    size: int
    data: str
    def __init__(self, *, type: FileType=..., name: str=..., size: int=..., data: str=...) -> None: ...

    def ClearField(self, field_name: Literal['type', 'name', 'size', 'data']) -> None: ...

class InfoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class InfoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    TOTAL_SPACE_FIELD_NUMBER: int
    FREE_SPACE_FIELD_NUMBER: int
    total_space: int
    free_space: int
    def __init__(self, *, total_space: int=..., free_space: int=...) -> None: ...

    def ClearField(self, field_name: Literal['total_space', 'free_space']) -> None: ...

class StatRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class StatResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILE_FIELD_NUMBER: int
    file: int
    def __init__(self, *, file: int=...) -> None: ...

    def ClearField(self, field_name: Literal['file']) -> None: ...

class ListRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class ListResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILE_FIELD_NUMBER: int
    file: int
    def __init__(self, *, file: int=...) -> None: ...

    def ClearField(self, field_name: Literal['file']) -> None: ...

class ReadRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class ReadResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    FILE_FIELD_NUMBER: int
    file: int
    def __init__(self, *, file: int=...) -> None: ...

    def ClearField(self, field_name: Literal['file']) -> None: ...

class WriteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    FILE_FIELD_NUMBER: int
    path: str
    file: int
    def __init__(self, *, path: str=..., file: int=...) -> None: ...

    def ClearField(self, field_name: Literal['path', 'file']) -> None: ...

class DeleteRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    RECURSIVE_FIELD_NUMBER: int
    path: str
    recursive: bool
    def __init__(self, *, path: str=..., recursive: bool=...) -> None: ...

    def ClearField(self, field_name: Literal['path', 'recursive']) -> None: ...

class MkdirRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class Md5sumRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class Md5sumResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MD5SUM_FIELD_NUMBER: int
    md5sum: str
    def __init__(self, *, md5sum: str=...) -> None: ...

    def ClearField(self, field_name: Literal['md5sum']) -> None: ...

class RenameRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    OLD_PATH_FIELD_NUMBER: int
    NEW_PATH_FIELD_NUMBER: int
    old_path: str
    new_path: str
    def __init__(self, *, old_path: str=..., new_path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['old_path', 'new_path']) -> None: ...

class BackupCreateRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ARCHIVE_PATH_FIELD_NUMBER: int
    archive_path: str
    def __init__(self, *, archive_path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['archive_path']) -> None: ...

class BackupRestoreRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ARCHIVE_PATH_FIELD_NUMBER: int
    archive_path: str
    def __init__(self, *, archive_path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['archive_path']) -> None: ...


    class enums:
        MetaEnum(name='FileType', values={'FILE': 0, 'DIR': 1})

class Gpio(MetaHelper):

    def __init__(self, client: Client):
        super().__init__("gpio", client)

class SetPinMode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    MODE_FIELD_NUMBER: int
    pin: GpioPin
    mode: GpioPinMode
    def __init__(self, *, pin: GpioPin=..., mode: GpioPinMode=...) -> None: ...

    def ClearField(self, field_name: Literal['pin', 'mode']) -> None: ...

class SetInputPull(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    PULL_MODE_FIELD_NUMBER: int
    pin: GpioPin
    pull_mode: GpioInputPull
    def __init__(self, *, pin: GpioPin=..., pull_mode: GpioInputPull=...) -> None: ...

    def ClearField(self, field_name: Literal['pin', 'pull_mode']) -> None: ...

class GetPinMode(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    pin: GpioPin
    def __init__(self, *, pin: GpioPin=...) -> None: ...

    def ClearField(self, field_name: Literal['pin']) -> None: ...

class GetPinModeResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    MODE_FIELD_NUMBER: int
    mode: GpioPinMode
    def __init__(self, *, mode: GpioPinMode=...) -> None: ...

    def ClearField(self, field_name: Literal['mode']) -> None: ...

class ReadPin(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    pin: GpioPin
    def __init__(self, *, pin: GpioPin=...) -> None: ...

    def ClearField(self, field_name: Literal['pin']) -> None: ...

class ReadPinResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    VALUE_FIELD_NUMBER: int
    value: int
    def __init__(self, *, value: int=...) -> None: ...

    def ClearField(self, field_name: Literal['value']) -> None: ...

class WritePin(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PIN_FIELD_NUMBER: int
    VALUE_FIELD_NUMBER: int
    pin: GpioPin
    value: int
    def __init__(self, *, pin: GpioPin=..., value: int=...) -> None: ...

    def ClearField(self, field_name: Literal['pin', 'value']) -> None: ...


    class enums:
        MetaEnum(name='GpioPin', values={'PC0': 0, 'PC1': 1, 'PC3': 2, 'PB2': 3, 'PB3': 4, 'PA4': 5, 'PA6': 6, 'PA7': 7})
        MetaEnum(name='GpioPinMode', values={'OUTPUT': 0, 'INPUT': 1})
        MetaEnum(name='GpioInputPull', values={'NO': 0, 'UP': 1, 'DOWN': 2})

class Application(MetaHelper):

    def __init__(self, client: Client):
        super().__init__("application", client)

class StartRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    NAME_FIELD_NUMBER: int
    ARGS_FIELD_NUMBER: int
    name: str
    args: str
    def __init__(self, *, name: str=..., args: str=...) -> None: ...

    def ClearField(self, field_name: Literal['name', 'args']) -> None: ...

class LockStatusRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class LockStatusResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    LOCKED_FIELD_NUMBER: int
    locked: bool
    def __init__(self, *, locked: bool=...) -> None: ...

    def ClearField(self, field_name: Literal['locked']) -> None: ...

class AppExitRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class AppLoadFileRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    PATH_FIELD_NUMBER: int
    path: str
    def __init__(self, *, path: str=...) -> None: ...

    def ClearField(self, field_name: Literal['path']) -> None: ...

class AppButtonPressRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    ARGS_FIELD_NUMBER: int
    args: str
    def __init__(self, *, args: str=...) -> None: ...

    def ClearField(self, field_name: Literal['args']) -> None: ...

class AppButtonReleaseRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    def __init__(self) -> None: ...

class AppStateResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor
    STATE_FIELD_NUMBER: int
    state: AppState
    def __init__(self, *, state: AppState=...) -> None: ...

    def ClearField(self, field_name: Literal['state']) -> None: ...


    class enums:
        MetaEnum(name='AppState', values={'APP_CLOSED': 0, 'APP_STARTED': 1})
