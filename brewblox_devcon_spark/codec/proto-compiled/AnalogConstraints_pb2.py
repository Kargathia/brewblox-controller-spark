# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: AnalogConstraints.proto

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


DESCRIPTOR = _descriptor.FileDescriptor(
  name='AnalogConstraints.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x17\x41nalogConstraints.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"{\n\x10\x41nalogConstraint\x12\x1b\n\x03min\x18\x01 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 H\x00\x12\x1b\n\x03max\x18\x02 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 H\x00\x12\x1f\n\x08\x62\x61lancer\x18\x03 \x01(\rB\x0b\x8a\xb5\x18\x02\x18\x06\x92?\x02\x38\x10H\x00\x42\x0c\n\nconstraint\"G\n\x11\x41nalogConstraints\x12\x32\n\x0b\x63onstraints\x18\x01 \x03(\x0b\x32\x16.blox.AnalogConstraintB\x05\x92?\x02\x10\x08\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_ANALOGCONSTRAINT = _descriptor.Descriptor(
  name='AnalogConstraint',
  full_name='blox.AnalogConstraint',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='blox.AnalogConstraint.min', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='blox.AnalogConstraint.max', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='balancer', full_name='blox.AnalogConstraint.balancer', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\002\030\006\222?\0028\020'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='constraint', full_name='blox.AnalogConstraint.constraint',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=63,
  serialized_end=186,
)


_ANALOGCONSTRAINTS = _descriptor.Descriptor(
  name='AnalogConstraints',
  full_name='blox.AnalogConstraints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='constraints', full_name='blox.AnalogConstraints.constraints', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\020\010'), file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=188,
  serialized_end=259,
)

_ANALOGCONSTRAINT.oneofs_by_name['constraint'].fields.append(
  _ANALOGCONSTRAINT.fields_by_name['min'])
_ANALOGCONSTRAINT.fields_by_name['min'].containing_oneof = _ANALOGCONSTRAINT.oneofs_by_name['constraint']
_ANALOGCONSTRAINT.oneofs_by_name['constraint'].fields.append(
  _ANALOGCONSTRAINT.fields_by_name['max'])
_ANALOGCONSTRAINT.fields_by_name['max'].containing_oneof = _ANALOGCONSTRAINT.oneofs_by_name['constraint']
_ANALOGCONSTRAINT.oneofs_by_name['constraint'].fields.append(
  _ANALOGCONSTRAINT.fields_by_name['balancer'])
_ANALOGCONSTRAINT.fields_by_name['balancer'].containing_oneof = _ANALOGCONSTRAINT.oneofs_by_name['constraint']
_ANALOGCONSTRAINTS.fields_by_name['constraints'].message_type = _ANALOGCONSTRAINT
DESCRIPTOR.message_types_by_name['AnalogConstraint'] = _ANALOGCONSTRAINT
DESCRIPTOR.message_types_by_name['AnalogConstraints'] = _ANALOGCONSTRAINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalogConstraint = _reflection.GeneratedProtocolMessageType('AnalogConstraint', (_message.Message,), dict(
  DESCRIPTOR = _ANALOGCONSTRAINT,
  __module__ = 'AnalogConstraints_pb2'
  # @@protoc_insertion_point(class_scope:blox.AnalogConstraint)
  ))
_sym_db.RegisterMessage(AnalogConstraint)

AnalogConstraints = _reflection.GeneratedProtocolMessageType('AnalogConstraints', (_message.Message,), dict(
  DESCRIPTOR = _ANALOGCONSTRAINTS,
  __module__ = 'AnalogConstraints_pb2'
  # @@protoc_insertion_point(class_scope:blox.AnalogConstraints)
  ))
_sym_db.RegisterMessage(AnalogConstraints)


_ANALOGCONSTRAINT.fields_by_name['min']._options = None
_ANALOGCONSTRAINT.fields_by_name['max']._options = None
_ANALOGCONSTRAINT.fields_by_name['balancer']._options = None
_ANALOGCONSTRAINTS.fields_by_name['constraints']._options = None
# @@protoc_insertion_point(module_scope)
