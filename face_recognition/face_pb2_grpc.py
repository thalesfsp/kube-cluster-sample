# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import face_pb2 as face__pb2


class IdentifyStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Identify = channel.unary_unary(
        '/face_recog.Identify/Identify',
        request_serializer=face__pb2.IdentifyRequest.SerializeToString,
        response_deserializer=face__pb2.IdentifyResponse.FromString,
        )


class IdentifyServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Identify(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_IdentifyServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Identify': grpc.unary_unary_rpc_method_handler(
          servicer.Identify,
          request_deserializer=face__pb2.IdentifyRequest.FromString,
          response_serializer=face__pb2.IdentifyResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'face_recog.Identify', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))