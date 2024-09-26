class FileManager:
    @staticmethod
    def save(content: str, file_path: str):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
