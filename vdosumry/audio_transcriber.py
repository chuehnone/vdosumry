import whisper


class AudioTranscriber:
    def __init__(self, model_size="base"):
        self.model_size = model_size

    def transcribe(self, video_path: str) -> str:
        model = whisper.load_model(self.model_size)
        response = model.transcribe(video_path)
        result = "\n".join(
            f"{i['id']}\n"
            f"{int(i['start'] // 3600):02}:{int((i['start'] % 3600) // 60):02}:{int(i['start'] % 60):02},"
            f"{int((i['start'] % 1) * 1000):03}"
            "--> "
            f"{int(i['end'] // 3600):02}:{int((i['end'] % 3600) // 60):02}:"
            f"{int(i['end'] % 60):02},{int((i['end'] % 1) * 1000):03}\n"
            f"{i['text'].strip()}\n"
            for i in response["segments"]
        )
        return result
