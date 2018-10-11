# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: ActuatorPwm.proto

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
  name='ActuatorPwm.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x41\x63tuatorPwm.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\x1a\x17\x41nalogConstraints.proto\"\xdb\x01\n\x0b\x41\x63tuatorPwm\x12\x1f\n\nactuatorId\x18\x01 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x05\x92?\x02\x38\x10\x12\x1d\n\ractuatorValid\x18\x02 \x01(\x08\x42\x06\x8a\xb5\x18\x02(\x01\x12\x0e\n\x06period\x18\x03 \x01(\r\x12#\n\x07setting\x18\x04 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12!\n\x05value\x18\x05 \x01(\x11\x42\x12\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \x8a\xb5\x18\x02(\x01\x12,\n\x0b\x63onstraints\x18\x06 \x01(\x0b\x32\x17.blox.AnalogConstraints:\x06\x92?\x03H\xb3\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,AnalogConstraints__pb2.DESCRIPTOR,])




_ACTUATORPWM = _descriptor.Descriptor(
  name='ActuatorPwm',
  full_name='blox.ActuatorPwm',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='actuatorId', full_name='blox.ActuatorPwm.actuatorId', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\005\222?\0028\020'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='actuatorValid', full_name='blox.ActuatorPwm.actuatorValid', index=1,
      number=2, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='period', full_name='blox.ActuatorPwm.period', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='setting', full_name='blox.ActuatorPwm.setting', index=3,
      number=4, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='blox.ActuatorPwm.value', index=4,
      number=5, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 \212\265\030\002(\001'), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='constraints', full_name='blox.ActuatorPwm.constraints', index=5,
      number=6, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\222?\003H\263\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=83,
  serialized_end=302,
)

_ACTUATORPWM.fields_by_name['constraints'].message_type = AnalogConstraints__pb2._ANALOGCONSTRAINTS
DESCRIPTOR.message_types_by_name['ActuatorPwm'] = _ACTUATORPWM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ActuatorPwm = _reflection.GeneratedProtocolMessageType('ActuatorPwm', (_message.Message,), dict(
  DESCRIPTOR = _ACTUATORPWM,
  __module__ = 'ActuatorPwm_pb2'
  # @@protoc_insertion_point(class_scope:blox.ActuatorPwm)
  ))
_sym_db.RegisterMessage(ActuatorPwm)


_ACTUATORPWM.fields_by_name['actuatorId']._options = None
_ACTUATORPWM.fields_by_name['actuatorValid']._options = None
_ACTUATORPWM.fields_by_name['setting']._options = None
_ACTUATORPWM.fields_by_name['value']._options = None
_ACTUATORPWM._options = None
# @@protoc_insertion_point(module_scope)
