# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import dsr_agent.agent_service_pb2 as agent__service__pb2


class AgentServiceStub(object):
    """The service definition.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SendSimpleMsgPack = channel.unary_unary(
                '/agent_service.AgentService/SendSimpleMsgPack',
                request_serializer=agent__service__pb2.SimplePackage.SerializeToString,
                response_deserializer=agent__service__pb2.ServerReply.FromString,
                )
        self.SendJsonMsgPack = channel.unary_unary(
                '/agent_service.AgentService/SendJsonMsgPack',
                request_serializer=agent__service__pb2.JsonMsgPack.SerializeToString,
                response_deserializer=agent__service__pb2.ServerReply.FromString,
                )


class AgentServiceServicer(object):
    """The service definition.
    """

    def SendSimpleMsgPack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SendJsonMsgPack(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AgentServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'SendSimpleMsgPack': grpc.unary_unary_rpc_method_handler(
                    servicer.SendSimpleMsgPack,
                    request_deserializer=agent__service__pb2.SimplePackage.FromString,
                    response_serializer=agent__service__pb2.ServerReply.SerializeToString,
            ),
            'SendJsonMsgPack': grpc.unary_unary_rpc_method_handler(
                    servicer.SendJsonMsgPack,
                    request_deserializer=agent__service__pb2.JsonMsgPack.FromString,
                    response_serializer=agent__service__pb2.ServerReply.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'agent_service.AgentService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AgentService(object):
    """The service definition.
    """

    @staticmethod
    def SendSimpleMsgPack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/agent_service.AgentService/SendSimpleMsgPack',
            agent__service__pb2.SimplePackage.SerializeToString,
            agent__service__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SendJsonMsgPack(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/agent_service.AgentService/SendJsonMsgPack',
            agent__service__pb2.JsonMsgPack.SerializeToString,
            agent__service__pb2.ServerReply.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
