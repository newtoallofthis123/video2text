# Video2Text

A simple GRPC service that transcribes an ytdl parsable video to text.
This uses the `yt-dlp` library to first parse the raw audio from the video link and then uses a
Whisper supported model to transcribe the audio to text.

You can customize your which model to use by changing the `model` variable for `WhisperTranscribe()`
in the `api/audio.py` file.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
