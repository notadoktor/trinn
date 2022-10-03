from google.protobuf.descriptor import FieldDescriptor


FIELD_TYPES = {
    FieldDescriptor.TYPE_DOUBLE: "float",
    FieldDescriptor.TYPE_FLOAT: "float",
    FieldDescriptor.TYPE_INT64: "int",
    FieldDescriptor.TYPE_UINT64: "int",
    FieldDescriptor.TYPE_INT32: "int",
    FieldDescriptor.TYPE_FIXED64: "int",
    FieldDescriptor.TYPE_FIXED32: "int",
    FieldDescriptor.TYPE_BOOL: "bool",
    FieldDescriptor.TYPE_STRING: "str",
    FieldDescriptor.TYPE_GROUP: "int",
    FieldDescriptor.TYPE_MESSAGE: "int",
    FieldDescriptor.TYPE_BYTES: "bytes",
    FieldDescriptor.TYPE_UINT32: "int",
    FieldDescriptor.TYPE_ENUM: "int",
    FieldDescriptor.TYPE_SFIXED32: "int",
    FieldDescriptor.TYPE_SFIXED64: "int",
    FieldDescriptor.TYPE_SINT32: "int",
    FieldDescriptor.TYPE_SINT64: "int",
}

CPP_TYPES = {
    FieldDescriptor.CPPTYPE_INT32: "int",
    FieldDescriptor.CPPTYPE_INT64: "int",
    FieldDescriptor.CPPTYPE_UINT32: "int",
    FieldDescriptor.CPPTYPE_UINT64: "int",
    FieldDescriptor.CPPTYPE_DOUBLE: "float",
    FieldDescriptor.CPPTYPE_FLOAT: "float",
    FieldDescriptor.CPPTYPE_BOOL: "bool",
    FieldDescriptor.CPPTYPE_ENUM: "int",
    FieldDescriptor.CPPTYPE_STRING: "str",
    FieldDescriptor.CPPTYPE_MESSAGE: "int",
}
