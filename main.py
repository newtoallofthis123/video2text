import grpc
from concurrent.futures import ThreadPoolExecutor
from api.audio import TranscriptionServiceServicer
import api.audio_pb2_grpc as audio_pb2_grpc

def serve():
    server = grpc.server(
        thread_pool=ThreadPoolExecutor(max_workers=10),
    )
    audio_server = TranscriptionServiceServicer()
    audio_pb2_grpc.add_TranscriptionServiceServicer_to_server(audio_server, server)

    server.add_insecure_port("[::]:50051")

    server.start()
    audio_server.logger.info("Audio server is running on port 50051...")

    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)


if __name__ == "__main__":
    serve()
