import os
from io import BytesIO

import yt_dlp
from pydub import AudioSegment


def get_audio_data(url: str) -> AudioSegment | None:
    try:
        ydl_opts = {
            "format": "bestaudio/best",
            "extract_audio": True,
            "outtmpl": "videos/%(title)s.%(ext)s",
            "noplaylist": True,
            "quiet": True,
            "no_warnings": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            if not info_dict:
                return None
            return convert_to_audio(
                f"videos/{info_dict['title']}.{info_dict['audio_ext']}", info_dict["audio_ext"]
            )

    except Exception as e:
        print(f"An error occurred: {e}")
        return None


def convert_to_audio(filename: str, ext: str) -> AudioSegment:
    with open(filename, "rb") as f:
        content = BytesIO(f.read())

    os.remove(filename)

    audio = AudioSegment.from_file(content, format=ext)
    return audio
