from api import audio_pb2
from api import audio_pb2_grpc
import logging
from vtt.whisper import WhisperTranscribe
from vtt.dl import get_audio_data

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

class TranscriptionServiceServicer(audio_pb2_grpc.TranscriptionServiceServicer):
    def __init__(self) -> None:
        self.logger = logging.getLogger(__name__)
        self.transcriber = WhisperTranscribe()

    def TranscribeAudio(self, request: audio_pb2.TranscriptionRequest, context):
        url = request.url
        audio = get_audio_data(url)
        transcriptions = self.transcriber.transcribe_audio(audio)
        for transcription in transcriptions:
            yield audio_pb2.TranscriptionResponse(status="success", message=transcription)
