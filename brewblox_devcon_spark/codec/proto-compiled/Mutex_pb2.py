# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: Mutex.proto

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
  name='Mutex.proto',
  package='blox',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x0bMutex.proto\x12\x04\x62lox\x1a\x0e\x62rewblox.proto\x1a\x0cnanopb.proto\".\n\x05Mutex\x12\x1d\n\x15\x64ifferentActuatorWait\x18\x01 \x01(\r:\x06\x92?\x03H\xb6\x02\x62\x06proto3')
  ,
  dependencies=[brewblox__pb2.DESCRIPTOR,nanopb__pb2.DESCRIPTOR,])




_MUTEX = _descriptor.Descriptor(
  name='Mutex',
  full_name='blox.Mutex',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='differentActuatorWait', full_name='blox.Mutex.differentActuatorWait', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('\222?\003H\266\002'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=51,
  serialized_end=97,
)

DESCRIPTOR.message_types_by_name['Mutex'] = _MUTEX
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

Mutex = _reflection.GeneratedProtocolMessageType('Mutex', (_message.Message,), dict(
  DESCRIPTOR = _MUTEX,
  __module__ = 'Mutex_pb2'
  # @@protoc_insertion_point(class_scope:blox.Mutex)
  ))
_sym_db.RegisterMessage(Mutex)


_MUTEX._options = None
# @@protoc_insertion_point(module_scope)
