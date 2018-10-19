# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorOffset.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


import brewblox_pb2 as brewblox__pb2
import nanopb_pb2 as nanopb__pb2
import AnalogConstraints_pb2 as AnalogConstraints__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='ActuatorOffset.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x14\x41\x63tuatorOffset.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x17\x41nalogConstraints.proto\"\xfe\x02\n\x0e\x41\x63tuatorOffset\x12\x1d\n\x08targetId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x01\x92?\x02\x38\x10\x12\x1b\n\x0btargetValid\x18\x02 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12 \n\x0breferenceId\x18\x03 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x01\x92?\x02\x38\x10\x12\x44\n\x17referenceSettingOrValue\x18\x04 \x01(\x0e\x32#.blox.ActuatorOffset.SettingOrValue\x12\x1e\n\x0ereferenceValid\x18\x05 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12#\n\x07setting\x18\x06 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12!\n\x05value\x18\x07 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12.\n\rconstrainedBy\x18\x08 \x01(\x0b\x32\x17.blox.AnalogConstraints\"(\n\x0eSettingOrValue\x12\x0b\n\x07SETTING\x10\x00\x12\t\n\x05VALUE\x10\x01:\x06\x92?\x03H\xb4\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,AnalogConstraints__pb2.DESCRIPTOR,])



_ACTUATOROFFSET_SETTINGORVALUE = _descriptor.EnumDescriptor(
  name='SettingOrValue',
  full_name='blox.ActuatorOffset.SettingOrValue',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='SETTING', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='VALUE', index=1, number=1,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=420,
  serialized_end=460,
)
_sym_db.RegisterEnumDescriptor(_ACTUATOROFFSET_SETTINGORVALUE)


_ACTUATOROFFSET = _descriptor.Descriptor(
  name='ActuatorOffset',
  full_name='blox.ActuatorOffset',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='targetId', full_name='blox.ActuatorOffset.targetId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\001\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='targetValid', full_name='blox.ActuatorOffset.targetValid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceId', full_name='blox.ActuatorOffset.referenceId', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\001\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceSettingOrValue', full_name='blox.ActuatorOffset.referenceSettingOrValue', index=3,
      number=4, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='referenceValid', full_name='blox.ActuatorOffset.referenceValid', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.ActuatorOffset.setting', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.ActuatorOffset.value', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constrainedBy', full_name='blox.ActuatorOffset.constrainedBy', index=7,
      number=8, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _ACTUATOROFFSET_SETTINGORVALUE,
  ],
  serialized_options=_b('\222?\003H\264\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=86,
  serialized_end=468,
)

_ACTUATOROFFSET.fields_by_name['referenceSettingOrValue'].enum_type = _ACTUATOROFFSET_SETTINGORVALUE
_ACTUATOROFFSET.fields_by_name['constrainedBy'].message_type = AnalogConstraints__pb2._ANALOGCONSTRAINTS
_ACTUATOROFFSET_SETTINGORVALUE.containing_type = _ACTUATOROFFSET
DESCRIPTOR.message_types_by_name['ActuatorOffset'] = _ACTUATOROFFSET
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActuatorOffset = _reflection.GeneratedProtocolMessageType('ActuatorOffset', (_message.Message,), dict(
  DESCRIPTOR = _ACTUATOROFFSET,
  __module__ = 'ActuatorOffset_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorOffset)
  ))
_sym_db.RegisterMessage(ActuatorOffset)


_ACTUATOROFFSET.fields_by_name['targetId']._options = None
_ACTUATOROFFSET.fields_by_name['targetValid']._options = None
_ACTUATOROFFSET.fields_by_name['referenceId']._options = None
_ACTUATOROFFSET.fields_by_name['referenceValid']._options = None
_ACTUATOROFFSET.fields_by_name['setting']._options = None
_ACTUATOROFFSET.fields_by_name['value']._options = None
_ACTUATOROFFSET._options = None
# @@protoc_insertion_point(module_scope)
