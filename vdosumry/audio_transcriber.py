import whisper


class AudioTranscriber:
    def __init__(self, model_size="base"):
        self.model_size = model_size
        self.segments = []

    def transcribe(self, video_path: str):
        model = whisper.load_model(self.model_size)
        response = model.transcribe(video_path)
        self.segments = response["segments"]

    def get_srt_format(self) -> str:
        return "\n".join(
            f"{i["id"] + 1}\n"
            f"{self._format_time(i["start"])} --> {self._format_time(i["end"])}\n"
            f"{i["text"].strip()}\n"
            for i in self.segments
        )

    def get_text_format(self) -> str:
        return "\n".join(i["text"].strip() for i in self.segments)

    @staticmethod
    def _format_time(seconds: float) -> str:
        hours = int(seconds // 3600)
        minutes = int((seconds % 3600) // 60)
        secs = int(seconds % 60)
        millis = int((seconds % 1) * 1000)
        return f"{hours:02}:{minutes:02}:{secs:02},{millis:03}"
