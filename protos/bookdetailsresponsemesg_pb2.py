# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: protos/bookdetailsresponsemesg.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from protos import bookdetailsfields_pb2 as protos_dot_bookdetailsfields__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='protos/bookdetailsresponsemesg.proto',
  package='',
  syntax='proto3',
  serialized_options=None,
  create_key=_descriptor._internal_create_key,
  serialized_pb=b'\n$protos/bookdetailsresponsemesg.proto\x1a\x1eprotos/bookdetailsfields.proto\"<\n\x17\x42ookDetailsResponseMesg\x12!\n\x05\x62ooks\x18\x01 \x03(\x0b\x32\x12.BookDetailsFieldsb\x06proto3'
  ,
  dependencies=[protos_dot_bookdetailsfields__pb2.DESCRIPTOR,])




_BOOKDETAILSRESPONSEMESG = _descriptor.Descriptor(
  name='BookDetailsResponseMesg',
  full_name='BookDetailsResponseMesg',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  create_key=_descriptor._internal_create_key,
  fields=[
    _descriptor.FieldDescriptor(
      name='books', full_name='BookDetailsResponseMesg.books', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR,  create_key=_descriptor._internal_create_key),
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
  serialized_start=72,
  serialized_end=132,
)

_BOOKDETAILSRESPONSEMESG.fields_by_name['books'].message_type = protos_dot_bookdetailsfields__pb2._BOOKDETAILSFIELDS
DESCRIPTOR.message_types_by_name['BookDetailsResponseMesg'] = _BOOKDETAILSRESPONSEMESG
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

BookDetailsResponseMesg = _reflection.GeneratedProtocolMessageType('BookDetailsResponseMesg', (_message.Message,), {
  'DESCRIPTOR' : _BOOKDETAILSRESPONSEMESG,
  '__module__' : 'protos.bookdetailsresponsemesg_pb2'
  # @@protoc_insertion_point(class_scope:BookDetailsResponseMesg)
  })
_sym_db.RegisterMessage(BookDetailsResponseMesg)


# @@protoc_insertion_point(module_scope)