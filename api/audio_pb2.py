# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# NO CHECKED-IN PROTOBUF GENCODE
# source: audio.proto
# Protobuf Python Version: 5.29.0
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import runtime_version as _runtime_version
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
_runtime_version.ValidateProtobufRuntimeVersion(
    _runtime_version.Domain.PUBLIC,
    5,
    29,
    0,
    '',
    'audio.proto'
)
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x61udio.proto\x12\x03\x61pi\"#\n\x14TranscriptionRequest\x12\x0b\n\x03url\x18\x01 \x01(\t\"8\n\x15TranscriptionResponse\x12\x0e\n\x06status\x18\x01 \x01(\t\x12\x0f\n\x07message\x18\x02 \x01(\t2b\n\x14TranscriptionService\x12J\n\x0fTranscribeAudio\x12\x19.api.TranscriptionRequest\x1a\x1a.api.TranscriptionResponse0\x01\x62\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'audio_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_TRANSCRIPTIONREQUEST']._serialized_start=20
  _globals['_TRANSCRIPTIONREQUEST']._serialized_end=55
  _globals['_TRANSCRIPTIONRESPONSE']._serialized_start=57
  _globals['_TRANSCRIPTIONRESPONSE']._serialized_end=113
  _globals['_TRANSCRIPTIONSERVICE']._serialized_start=115
  _globals['_TRANSCRIPTIONSERVICE']._serialized_end=213
# @@protoc_insertion_point(module_scope)
