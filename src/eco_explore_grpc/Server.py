import grpc 
import comentarios_pb2_grpc
from concurrent import futures 

def Server():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    comentarios_pb2_grpc.add_ComentariosServiceServicer_to_server(comentarios_pb2_grpc.ComentariosServiceServicer(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Empezó")
    server.wait_for_termination()
    print("Terminó")

if __name__ == '__main__':
    Server()
