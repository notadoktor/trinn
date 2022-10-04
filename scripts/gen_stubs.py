#!/usr/bin/env python3

""" Generates not 100% accurate stubs, but they let vscode intellisense actually work """

from __future__ import annotations

import datetime
import importlib
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

import typer
from google.protobuf.descriptor import Descriptor, EnumDescriptor, FieldDescriptor

LIB_PATH = Path(__file__).resolve().parents[1] / "src"
if str(LIB_PATH) not in sys.path:
    sys.path.insert(0, str(LIB_PATH))
from trinn.sensors.flipper.util import FIELD_TYPES

MOD_PREFIX = "trinn.sensors.flipper"
SRC_DIR = LIB_PATH / MOD_PREFIX.replace(".", "/")
TAB = " " * 4

STUB_IMPORTS = [
    "from __future__ import annotations",
    "from enum import IntEnum",
    "from typing import Literal",
    "import google.protobuf.descriptor",
    "import google.protobuf.message",
    "import google.protobuf.symbol_database",
]
GENERIC_GLOBALS = [
    "DESCRIPTOR: google.protobuf.descriptor.FileDescriptor",
    "_sym_db: google.protobuf.symbol_database.SymbolDatabase",
]


@dataclass(order=True, frozen=True)
class MetaProtobuf:
    src_file: Path
    commands: list[MetaMessage] = field(default_factory=list)
    enums: list[MetaEnum] = field(default_factory=list)

    @property
    def name(self):
        return self.src_file.stem[:-4]  # remove _pb2

    @classmethod
    def from_file(cls, src_file: Path) -> MetaProtobuf:
        mod = importlib.import_module(f"{MOD_PREFIX}.{src_file.stem}")
        meta = cls(src_file)
        for name, obj in mod.__dict__.items():
            if isinstance(obj, Descriptor):
                meta.add_command(obj)
            elif isinstance(obj, EnumDescriptor):
                meta.add_enum(obj)
        return meta

    @property
    def imports(self):
        imports = set()
        for cmd in self.commands:
            imports.update(cmd.imports)
        return STUB_IMPORTS + [f"import trinn.sensors.flipper.{i}" for i in sorted(imports)]

    @property
    def header(self) -> list[str]:
        docstring = f'"""\nThis file was auto-generated by {Path(__file__).name}\n"""\n'
        return [docstring, *self.imports, *GENERIC_GLOBALS]

    def add_command(self, cmd: Descriptor):
        meta_msg = MetaMessage.from_message(cmd)
        self.commands.append(meta_msg)

    def add_enum(self, enum: EnumDescriptor):
        meta_enum = MetaEnum.from_enum(enum)
        self.enums.append(meta_enum)

    def write(self):
        stub = self.src_file.parent / f"{self.src_file.stem}.pyi"
        stub.write_text(str(self) + "\n")
        for post in ["isort", "black"]:
            subprocess.run([post, str(stub)], check=True, capture_output=True)
        print(f"Generated {stub.relative_to(LIB_PATH)}", file=sys.stderr)

    def __str__(self) -> str:
        header_str = "\n".join(self.header)
        commands = "\n".join([c.print() for c in self.commands])
        enums = "\n".join([e.print() for e in self.enums])

        return "\n".join([header_str, commands, enums])


@dataclass(frozen=True, order=True)
class MetaMessage:
    name: str
    fields: dict[str, str] = field(default_factory=dict)
    imports: set[str] = field(default_factory=set)

    def add_field(self, field: FieldDescriptor):
        if field.enum_type:
            field_type = field.enum_type.name
        elif field.type == FieldDescriptor.TYPE_MESSAGE:
            pkg, name = field.message_type.full_name.split(".", 1)
            if pkg == "PB":
                field_type = field.message_type.name
            else:
                mod_name = pkg.split("_", 1)[-1].lower() + "_pb2"
                if mod_name == "app_pb2":
                    mod_name = "application_pb2"
                self.imports.add(mod_name)
                field_type = f"trinn.sensors.flipper.{mod_name}.{name}"
        elif field.type == FieldDescriptor.TYPE_BYTES:
            field_type = "bytes"
        else:
            field_type = FIELD_TYPES[field.type]
        self.fields[field.name] = field_type

    @classmethod
    def from_message(cls, msg: Descriptor):
        meta_msg = cls(msg.name)
        for field in msg.fields:
            meta_msg.add_field(field)
        return meta_msg

    def print(self, *, indent: int = 0) -> str:
        class_str = [f"{TAB * indent}class {self.name}(google.protobuf.message.Message):"]

        attrs = [f"{TAB * (indent+1)}DESCRIPTOR: google.protobuf.descriptor.Descriptor"]

        init_str = f"{TAB *(indent+1)}def __init__(self"
        if self.fields:
            init_str += ", *"
            for field in self.fields:
                attrs.append(f"{TAB*(indent+1)}{field.upper()}_FIELD_NUMBER: int")
                init_str += f", {field}: {self.fields[field]} = ..."
        init_str += ") -> None: ..."
        attrs.extend([f"{TAB * (indent+1)}{f}: {t}" for f, t in self.fields.items()])

        class_str.extend(attrs)
        class_str.append(init_str)
        if self.fields:
            clear_str = f"{TAB*(indent+1)}def ClearField(self, field_name: Literal{list(self.fields.keys())}) -> None: ..."
            class_str.append(clear_str)

        return "\n".join(class_str)


@dataclass(frozen=True, order=True)
class MetaEnum:
    name: str
    values: dict[str, int] = field(default_factory=dict)

    def print(self, *, indent: int = 0) -> str:
        class_str = [f"{TAB * indent}class {self.name}(IntEnum):"]
        key_globals = []
        for k, v in self.values.items():
            class_str.append(f"{TAB * (indent + 1)}{k} = {v}")
            key_globals.append(f"{k} = {self.name}.{k}")
        return "\n".join(class_str + key_globals)

    @classmethod
    def from_enum(cls, enum: EnumDescriptor) -> MetaEnum:
        return cls(enum.name, {v.name: v.number for v in enum.values})


def ts(spec="seconds"):
    return datetime.datetime.now().isoformat(timespec=spec)


def cc_to_snake(name: str) -> str:
    new_name = ""
    for i in range(len(name)):
        if i > 0 and name[i].isupper():
            if name[i - 1].islower():
                new_name += "_"
            elif i < len(name) - 1 and name[i + 1].islower():
                new_name += "_"
        new_name += name[i].lower()
    return new_name


def main():
    proto_files = [p.resolve() for p in SRC_DIR.glob("*_pb2.py") if p.is_file()]

    for proto_file in proto_files:
        pf_cmd = MetaProtobuf.from_file(proto_file)
        pf_cmd.write()

    print(
        f"{ts()} - Finished generating all type stubs",
        file=sys.stderr,
    )


###

if __name__ == "__main__":
    typer.run(main)
