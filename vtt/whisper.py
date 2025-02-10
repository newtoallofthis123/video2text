from typing import Generator
import torch
import numpy as np
import wave
import io
from transformers import WhisperProcessor, WhisperForConditionalGeneration
from pydub import AudioSegment

class WhisperTranscribe:
    def __init__(self, model="openai/whisper-small") -> None:
        processor = WhisperProcessor.from_pretrained(model)
        if isinstance(processor, WhisperProcessor):
            self.processor = processor
        else:
            self.processor = processor[0]
        self.model = WhisperForConditionalGeneration.from_pretrained(
            "openai/whisper-small"
        )
        # Disable forced decoder IDs to allow language detection
        self.model.config.forced_decoder_ids = None

    def split_audio_into_chunks(self, audio_data, sample_rate, chunk_duration=30):
        chunk_size = chunk_duration * sample_rate
        return [
            audio_data[i : i + chunk_size]
            for i in range(0, len(audio_data), chunk_size)
        ]

    def cal_chunk_size(self, audio_data, seconds=30):
        try:
            with wave.open(io.BytesIO(audio_data), "rb") as wav_file:
                sample_rate = wav_file.getframerate()
                bit_depth = wav_file.getsampwidth() * 8
                num_channels = wav_file.getnchannels()
                bytes_per_second = (sample_rate * bit_depth * num_channels) // 8
                return bytes_per_second * seconds
        except wave.Error as e:
            print(f"Not enough data to parse WAV header: {e}")
            return 0

    def transcribe_audio(self, audio_data: AudioSegment) -> Generator[str, None, None]:
        audio = audio_data.set_frame_rate(16000).set_channels(1).set_sample_width(2)
        wave_data = audio.export(format="wav").read()
        chunk_size = self.cal_chunk_size(wave_data)

        while len(wave_data) >= chunk_size:
            chunk = wave_data[:chunk_size]
            wave_data = wave_data[chunk_size:]

            print("Transcribing 30-second chunk...")
            transcription = str(self.transcribe_audio_chunk(chunk))
            yield transcription

        if wave_data:
            print("Transcribing remaining audio...")
            yield str(self.transcribe_audio_chunk(wave_data))

    def transcribe_audio_chunk(self, chunk, sample_rate=16000) -> str:
        audio_array = np.frombuffer(chunk, dtype=np.int16).astype(np.float32)

        audio_array /= np.iinfo(np.int16).max

        inputs = self.processor(
            audio_array, sampling_rate=sample_rate, return_tensors="pt"
        )

        with torch.no_grad():
            predicted_ids = self.model.generate(inputs["input_features"])

        transcription = self.processor.batch_decode(
            predicted_ids, skip_special_tokens=True
        )[0]
        return str(transcription)
