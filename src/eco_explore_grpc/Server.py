import grpc
import comentarios_pb2
import comentarios_pb2_grpc
from concurrent import futures
from documentdb.document_operation import getComentario

class ComentariosService(comentarios_pb2_grpc.ComentariosServiceServicer):

    def ObtenerComentario(self, request, context):
        comentario_id = request.id 
        comentario = getComentario(comentario_id)
        if comentario:
            comentario_proto = comentarios_pb2.Comentario(
                evaluacion=comentario.Evaluacion,
                comentario=comentario.Comentario
            )
            return comentarios_pb2.returnComentario(comentario=[comentario_proto])
        else:
            return comentarios_pb2.returnComentario()

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comentarios_pb2_grpc.add_ComentariosServiceServicer_to_server(ComentariosService(), server)
    server.add_insecure_port('localhost:50059')
    server.start()
    print("Servidor gRPC iniciado en el puerto 50059")
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
