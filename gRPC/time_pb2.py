# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: time.proto
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import wrappers_pb2 as google_dot_protobuf_dot_wrappers__pb2
from google.api import annotations_pb2 as google_dot_api_dot_annotations__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\ntime.proto\x12\x04time\x1a\x1egoogle/protobuf/wrappers.proto\x1a\x1cgoogle/api/annotations.proto2b\n\x04Time\x12Z\n\x03now\x12\x1c.google.protobuf.StringValue\x1a\x1c.google.protobuf.StringValue\"\x17\x82\xd3\xe4\x93\x02\x11\x12\x0c/v1/time/now:\x01*b\x06proto3')



_TIME = DESCRIPTOR.services_by_name['Time']
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _TIME.methods_by_name['now']._options = None
  _TIME.methods_by_name['now']._serialized_options = b'\202\323\344\223\002\021\022\014/v1/time/now:\001*'
  _TIME._serialized_start=82
  _TIME._serialized_end=180
# @@protoc_insertion_point(module_scope)