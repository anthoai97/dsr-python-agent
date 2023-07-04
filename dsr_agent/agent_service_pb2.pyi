from google.protobuf import timestamp_pb2 as _timestamp_pb2
from google.protobuf import struct_pb2 as _struct_pb2
from google.protobuf.internal import containers as _containers
from google.protobuf.internal import enum_type_wrapper as _enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class MessageType(int, metaclass=_enum_type_wrapper.EnumTypeWrapper):
    __slots__ = []
    LOG: _ClassVar[MessageType]
    RESULT: _ClassVar[MessageType]
LOG: MessageType
RESULT: MessageType

class PackageMetadata(_message.Message):
    __slots__ = ["agent", "agent_id", "timestamp", "resend", "message_id", "type"]
    AGENT_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    TIMESTAMP_FIELD_NUMBER: _ClassVar[int]
    RESEND_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    TYPE_FIELD_NUMBER: _ClassVar[int]
    agent: str
    agent_id: str
    timestamp: _timestamp_pb2.Timestamp
    resend: int
    message_id: str
    type: MessageType
    def __init__(self, agent: _Optional[str] = ..., agent_id: _Optional[str] = ..., timestamp: _Optional[_Union[_timestamp_pb2.Timestamp, _Mapping]] = ..., resend: _Optional[int] = ..., message_id: _Optional[str] = ..., type: _Optional[_Union[MessageType, str]] = ...) -> None: ...

class SimplePackage(_message.Message):
    __slots__ = ["metadata", "data"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    metadata: PackageMetadata
    data: _containers.RepeatedScalarFieldContainer[str]
    def __init__(self, metadata: _Optional[_Union[PackageMetadata, _Mapping]] = ..., data: _Optional[_Iterable[str]] = ...) -> None: ...

class JsonMsgPack(_message.Message):
    __slots__ = ["metadata", "data"]
    METADATA_FIELD_NUMBER: _ClassVar[int]
    DATA_FIELD_NUMBER: _ClassVar[int]
    metadata: PackageMetadata
    data: _containers.RepeatedCompositeFieldContainer[_struct_pb2.Struct]
    def __init__(self, metadata: _Optional[_Union[PackageMetadata, _Mapping]] = ..., data: _Optional[_Iterable[_Union[_struct_pb2.Struct, _Mapping]]] = ...) -> None: ...

class ServerReply(_message.Message):
    __slots__ = ["reply"]
    REPLY_FIELD_NUMBER: _ClassVar[int]
    reply: _containers.RepeatedCompositeFieldContainer[PackageExcuteStatus]
    def __init__(self, reply: _Optional[_Iterable[_Union[PackageExcuteStatus, _Mapping]]] = ...) -> None: ...

class PackageExcuteStatus(_message.Message):
    __slots__ = ["success", "agent_id", "message_id", "path", "error"]
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    AGENT_ID_FIELD_NUMBER: _ClassVar[int]
    MESSAGE_ID_FIELD_NUMBER: _ClassVar[int]
    PATH_FIELD_NUMBER: _ClassVar[int]
    ERROR_FIELD_NUMBER: _ClassVar[int]
    success: bool
    agent_id: str
    message_id: str
    path: str
    error: str
    def __init__(self, success: bool = ..., agent_id: _Optional[str] = ..., message_id: _Optional[str] = ..., path: _Optional[str] = ..., error: _Optional[str] = ...) -> None: ...
