# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import comentarios_pb2 as comentarios__pb2


class ComentariosServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PublicarComentario = channel.unary_unary(
                '/Comentarios.ComentariosService/PublicarComentario',
                request_serializer=comentarios__pb2.Comentario.SerializeToString,
                response_deserializer=comentarios__pb2.Respuesta.FromString,
                )
        self.ObtenerComentarios = channel.unary_unary(
                '/Comentarios.ComentariosService/ObtenerComentarios',
                request_serializer=comentarios__pb2.ConsultaComentarios.SerializeToString,
                response_deserializer=comentarios__pb2.ListaComentarios.FromString,
                )


class ComentariosServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PublicarComentario(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ObtenerComentarios(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ComentariosServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PublicarComentario': grpc.unary_unary_rpc_method_handler(
                    servicer.PublicarComentario,
                    request_deserializer=comentarios__pb2.Comentario.FromString,
                    response_serializer=comentarios__pb2.Respuesta.SerializeToString,
            ),
            'ObtenerComentarios': grpc.unary_unary_rpc_method_handler(
                    servicer.ObtenerComentarios,
                    request_deserializer=comentarios__pb2.ConsultaComentarios.FromString,
                    response_serializer=comentarios__pb2.ListaComentarios.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Comentarios.ComentariosService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ComentariosService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PublicarComentario(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Comentarios.ComentariosService/PublicarComentario',
            comentarios__pb2.Comentario.SerializeToString,
            comentarios__pb2.Respuesta.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ObtenerComentarios(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Comentarios.ComentariosService/ObtenerComentarios',
            comentarios__pb2.ConsultaComentarios.SerializeToString,
            comentarios__pb2.ListaComentarios.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)