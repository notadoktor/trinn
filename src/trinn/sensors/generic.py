from abc import ABC, abstractmethod
from typing import ClassVar

from serial import Serial


class GenericClient(ABC):
    _serial: Serial
    _type: ClassVar[str] = "generic"

    def __str__(self) -> str:
        extra_info = self._str_info()
        if extra_info:
            extra_info = f" {extra_info}"
        return f"<TrinnClient type={self._type} src={self._serial}{extra_info}>"

    def _str_info(self) -> str:
        return ""

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def poll(self, interval: int):
        pass

    