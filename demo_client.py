import logging

import grpc
import demo_pb2
import demo_pb2_grpc



def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = demo_pb2_grpc.DemoStub(channel)
        print("-------------- Send Message --------------")
        print(stub.SendMessage(demo_pb2.messageInput()))






if __name__ == '__main__':
    logging.basicConfig()
    run()