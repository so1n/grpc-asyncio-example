import logging
import time
from concurrent import futures

import grpc

from grpc_asyncio_example.protos import helloworld_pb2, helloworld_pb2_grpc


class Greeter(helloworld_pb2_grpc.GreeterServicer):
    def SayHello(
        self, request: helloworld_pb2.HelloRequest, context: grpc.ServicerContext
    ) -> helloworld_pb2.HelloReply:
        time.sleep(request.sleep_millisecond / 1000)
        return helloworld_pb2.HelloReply(message="Hello, %s!" % request.name)


def serve(target: str = "localhost:9999") -> grpc.server:
    server: grpc.server = grpc.server(futures.ThreadPoolExecutor(max_workers=100))
    helloworld_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port(target)
    server.start()
    return server


if __name__ == "__main__":
    logging.basicConfig()
    serve().wait_for_termination()
