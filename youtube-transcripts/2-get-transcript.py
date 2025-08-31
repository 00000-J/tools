import argparse
import glob
import os
from typing import Optional

import whisper


def find_most_recent_audio() -> Optional[str]:
    extensions = ("*.mp3", "*.flac", "*.m4a", "*.wav", "*.mp4", "*.mkv")
    candidates = []
    for pattern in extensions:
        candidates.extend(glob.glob(pattern))
    if not candidates:
        return None
    candidates.sort(key=lambda p: os.path.getmtime(p), reverse=True)
    return candidates[0]


def main() -> None:
    parser = argparse.ArgumentParser(description="Transcribe an audio/video file with Whisper")
    parser.add_argument("--audio", type=str, default=None, help="Path to audio/video file (mp3/flac/wav/mp4)")
    parser.add_argument("--model", type=str, default="small", help="Whisper model size: tiny, base, small, medium, large")
    parser.add_argument("--output", type=str, default=None, help="Output text file (defaults to <audio_basename>.txt)")
    args = parser.parse_args()

    audio_path = args.audio
    if audio_path is None:
        audio_path = find_most_recent_audio()
        if audio_path is None:
            raise FileNotFoundError("No audio/video file found. Provide --audio path or place an mp3/flac in this folder.")

    output_path = args.output or f"{os.path.splitext(os.path.basename(audio_path))[0]}.txt"
    print(f"Transcribing: {audio_path}")
    model = whisper.load_model(args.model)
    result = model.transcribe(audio_path)

    with open(output_path, "w") as f:
        f.write(result["text"])
    print(f"Saved transcript to {output_path}")


if __name__ == "__main__":
    main()
