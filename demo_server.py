import logging
from concurrent import futures

import demo_pb2_grpc
import grpc
import demo_pb2


class DemoServicer(demo_pb2_grpc.DemoServicer):

    def SendMessage(self, request, context):

        return demo_pb2.messageOutput(msg="A message from CS361")

def serve():
  server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
  demo_pb2_grpc.add_DemoServicer_to_server(
      DemoServicer(), server)
  server.add_insecure_port('[::]:50051')
  server.start()
  server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()