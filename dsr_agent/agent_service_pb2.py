# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: agent_service.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2
from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x13\x61gent_service.proto\x12\ragent_service\x1a\x1fgoogle/protobuf/timestamp.proto\x1a\x1cgoogle/protobuf/struct.proto\"\xaf\x01\n\x0fPackageMetadata\x12\r\n\x05\x61gent\x18\x01 \x01(\t\x12\x10\n\x08\x61gent_id\x18\x02 \x01(\t\x12-\n\ttimestamp\x18\x03 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0e\n\x06resend\x18\x04 \x01(\x05\x12\x12\n\nmessage_id\x18\x05 \x01(\t\x12(\n\x04type\x18\x06 \x01(\x0e\x32\x1a.agent_service.MessageType\"O\n\rSimplePackage\x12\x30\n\x08metadata\x18\x01 \x01(\x0b\x32\x1e.agent_service.PackageMetadata\x12\x0c\n\x04\x64\x61ta\x18\x02 \x03(\t\"f\n\x0bJsonMsgPack\x12\x30\n\x08metadata\x18\x01 \x01(\x0b\x32\x1e.agent_service.PackageMetadata\x12%\n\x04\x64\x61ta\x18\x02 \x03(\x0b\x32\x17.google.protobuf.Struct\"@\n\x0bServerReply\x12\x31\n\x05reply\x18\x01 \x03(\x0b\x32\".agent_service.PackageExcuteStatus\"i\n\x13PackageExcuteStatus\x12\x0f\n\x07success\x18\x01 \x01(\x08\x12\x10\n\x08\x61gent_id\x18\x02 \x01(\t\x12\x12\n\nmessage_id\x18\x03 \x01(\t\x12\x0c\n\x04path\x18\x04 \x01(\t\x12\r\n\x05\x65rror\x18\x05 \x01(\t*\"\n\x0bMessageType\x12\x07\n\x03LOG\x10\x00\x12\n\n\x06RESULT\x10\x01\x32\xac\x01\n\x0c\x41gentService\x12O\n\x11SendSimpleMsgPack\x12\x1c.agent_service.SimplePackage\x1a\x1a.agent_service.ServerReply\"\x00\x12K\n\x0fSendJsonMsgPack\x12\x1a.agent_service.JsonMsgPack\x1a\x1a.agent_service.ServerReply\"\x00\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'agent_service_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _globals['_MESSAGETYPE']._serialized_start=637
  _globals['_MESSAGETYPE']._serialized_end=671
  _globals['_PACKAGEMETADATA']._serialized_start=102
  _globals['_PACKAGEMETADATA']._serialized_end=277
  _globals['_SIMPLEPACKAGE']._serialized_start=279
  _globals['_SIMPLEPACKAGE']._serialized_end=358
  _globals['_JSONMSGPACK']._serialized_start=360
  _globals['_JSONMSGPACK']._serialized_end=462
  _globals['_SERVERREPLY']._serialized_start=464
  _globals['_SERVERREPLY']._serialized_end=528
  _globals['_PACKAGEEXCUTESTATUS']._serialized_start=530
  _globals['_PACKAGEEXCUTESTATUS']._serialized_end=635
  _globals['_AGENTSERVICE']._serialized_start=674
  _globals['_AGENTSERVICE']._serialized_end=846
# @@protoc_insertion_point(module_scope)
