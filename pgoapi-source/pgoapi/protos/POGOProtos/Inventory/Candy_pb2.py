# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: POGOProtos/Inventory/Candy.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from POGOProtos.Enums import PokemonFamilyId_pb2 as POGOProtos_dot_Enums_dot_PokemonFamilyId__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='POGOProtos/Inventory/Candy.proto',
  package='POGOProtos.Inventory',
  syntax='proto3',
  serialized_pb=_b('\n POGOProtos/Inventory/Candy.proto\x12\x14POGOProtos.Inventory\x1a&POGOProtos/Enums/PokemonFamilyId.proto\"L\n\x05\x43\x61ndy\x12\x34\n\tfamily_id\x18\x01 \x01(\x0e\x32!.POGOProtos.Enums.PokemonFamilyId\x12\r\n\x05\x63\x61ndy\x18\x02 \x01(\x05\x62\x06proto3')
  ,
  dependencies=[POGOProtos_dot_Enums_dot_PokemonFamilyId__pb2.DESCRIPTOR,])
_sym_db.RegisterFileDescriptor(DESCRIPTOR)




_CANDY = _descriptor.Descriptor(
  name='Candy',
  full_name='POGOProtos.Inventory.Candy',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='family_id', full_name='POGOProtos.Inventory.Candy.family_id', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='candy', full_name='POGOProtos.Inventory.Candy.candy', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=98,
  serialized_end=174,
)

_CANDY.fields_by_name['family_id'].enum_type = POGOProtos_dot_Enums_dot_PokemonFamilyId__pb2._POKEMONFAMILYID
DESCRIPTOR.message_types_by_name['Candy'] = _CANDY

Candy = _reflection.GeneratedProtocolMessageType('Candy', (_message.Message,), dict(
  DESCRIPTOR = _CANDY,
  __module__ = 'POGOProtos.Inventory.Candy_pb2'
  # @@protoc_insertion_point(class_scope:POGOProtos.Inventory.Candy)
  ))
_sym_db.RegisterMessage(Candy)


# @@protoc_insertion_point(module_scope)