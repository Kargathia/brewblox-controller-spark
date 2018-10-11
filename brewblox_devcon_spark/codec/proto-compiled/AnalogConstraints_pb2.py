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
  serialized_pb=_b('\n\x17\x41nalogConstraints.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\"*\n\rConstraintMin\x12\x19\n\x03min\x18\x01 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \"*\n\rConstraintMax\x12\x19\n\x03max\x18\x01 \x01(\x11\x42\x0c\x8a\xb5\x18\x03\x10\x80 \x92?\x02\x38 \"i\n\x11\x43onstraintWrapper\x12\"\n\x03min\x18\x01 \x01(\x0b\x32\x13.blox.ConstraintMinH\x00\x12\"\n\x03max\x18\x02 \x01(\x0b\x32\x13.blox.ConstraintMaxH\x00\x42\x0c\n\nconstraint\"G\n\x11\x41nalogConstraints\x12\x32\n\nconstraint\x18\x01 \x03(\x0b\x32\x17.blox.ConstraintWrapperB\x05\x92?\x02\x10\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_CONSTRAINTMIN = _descriptor.Descriptor(
  name='ConstraintMin',
  full_name='blox.ConstraintMin',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='blox.ConstraintMin.min', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
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
  serialized_start=63,
  serialized_end=105,
)


_CONSTRAINTMAX = _descriptor.Descriptor(
  name='ConstraintMax',
  full_name='blox.ConstraintMax',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='max', full_name='blox.ConstraintMax.max', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\212\265\030\003\020\200 \222?\0028 '), file=DESCRIPTOR),
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
  serialized_start=107,
  serialized_end=149,
)


_CONSTRAINTWRAPPER = _descriptor.Descriptor(
  name='ConstraintWrapper',
  full_name='blox.ConstraintWrapper',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='min', full_name='blox.ConstraintWrapper.min', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='max', full_name='blox.ConstraintWrapper.max', index=1,
      number=2, type=11, cpp_type=10, label=1,
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
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
    _descriptor.OneofDescriptor(
      name='constraint', full_name='blox.ConstraintWrapper.constraint',
      index=0, containing_type=None, fields=[]),
  ],
  serialized_start=151,
  serialized_end=256,
)


_ANALOGCONSTRAINTS = _descriptor.Descriptor(
  name='AnalogConstraints',
  full_name='blox.AnalogConstraints',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='constraint', full_name='blox.AnalogConstraints.constraint', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=_b('\222?\002\020\002'), file=DESCRIPTOR),
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
  serialized_start=258,
  serialized_end=329,
)

_CONSTRAINTWRAPPER.fields_by_name['min'].message_type = _CONSTRAINTMIN
_CONSTRAINTWRAPPER.fields_by_name['max'].message_type = _CONSTRAINTMAX
_CONSTRAINTWRAPPER.oneofs_by_name['constraint'].fields.append(
  _CONSTRAINTWRAPPER.fields_by_name['min'])
_CONSTRAINTWRAPPER.fields_by_name['min'].containing_oneof = _CONSTRAINTWRAPPER.oneofs_by_name['constraint']
_CONSTRAINTWRAPPER.oneofs_by_name['constraint'].fields.append(
  _CONSTRAINTWRAPPER.fields_by_name['max'])
_CONSTRAINTWRAPPER.fields_by_name['max'].containing_oneof = _CONSTRAINTWRAPPER.oneofs_by_name['constraint']
_ANALOGCONSTRAINTS.fields_by_name['constraint'].message_type = _CONSTRAINTWRAPPER
DESCRIPTOR.message_types_by_name['ConstraintMin'] = _CONSTRAINTMIN
DESCRIPTOR.message_types_by_name['ConstraintMax'] = _CONSTRAINTMAX
DESCRIPTOR.message_types_by_name['ConstraintWrapper'] = _CONSTRAINTWRAPPER
DESCRIPTOR.message_types_by_name['AnalogConstraints'] = _ANALOGCONSTRAINTS
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ConstraintMin = _reflection.GeneratedProtocolMessageType('ConstraintMin', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINTMIN,
  __module__ = 'AnalogConstraints_pb2'
  # @@protoc_insertion_point(class_scope:blox.ConstraintMin)
  ))
_sym_db.RegisterMessage(ConstraintMin)

ConstraintMax = _reflection.GeneratedProtocolMessageType('ConstraintMax', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINTMAX,
  __module__ = 'AnalogConstraints_pb2'
  # @@protoc_insertion_point(class_scope:blox.ConstraintMax)
  ))
_sym_db.RegisterMessage(ConstraintMax)

ConstraintWrapper = _reflection.GeneratedProtocolMessageType('ConstraintWrapper', (_message.Message,), dict(
  DESCRIPTOR = _CONSTRAINTWRAPPER,
  __module__ = 'AnalogConstraints_pb2'
  # @@protoc_insertion_point(class_scope:blox.ConstraintWrapper)
  ))
_sym_db.RegisterMessage(ConstraintWrapper)

AnalogConstraints = _reflection.GeneratedProtocolMessageType('AnalogConstraints', (_message.Message,), dict(
  DESCRIPTOR = _ANALOGCONSTRAINTS,
  __module__ = 'AnalogConstraints_pb2'
  # @@protoc_insertion_point(class_scope:blox.AnalogConstraints)
  ))
_sym_db.RegisterMessage(AnalogConstraints)


_CONSTRAINTMIN.fields_by_name['min']._options = None
_CONSTRAINTMAX.fields_by_name['max']._options = None
_ANALOGCONSTRAINTS.fields_by_name['constraint']._options = None
# @@protoc_insertion_point(module_scope)
