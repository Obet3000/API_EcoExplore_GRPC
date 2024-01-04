import grpc
import comentarios_pb2
import comentarios_pb2_grpc
from concurrent import futures

class ComentariosService(comentarios_pb2_grpc.ComentariosServiceServicer):
    def PublicarComentario(self, request, context):
        return comentarios_pb2.Respuesta(exito=True, mensaje="Comentario publicado exitosamente")

    def ObtenerComentarios(self, request, context):
        comentarios = [
            comentarios_pb2.Comentario(autor="Usuario1", contenido="¡Gran comentario!"),
            comentarios_pb2.Comentario(autor="Usuario2", contenido="Otro comentario interesante"),
        ]
        return comentarios_pb2.ListaComentarios(comentarios=comentarios)

def run_server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comentarios_pb2_grpc.add_ComentariosServiceServicer_to_server(ComentariosService(), server)
    server.add_insecure_port('localhost:50059')
    server.start()
    print("Servidor gRPC iniciado en el puerto 50059")
    server.wait_for_termination()

if __name__ == '__main__':
    run_server()
