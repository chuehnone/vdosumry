from pathlib import Path
import shutil


class FileManager:
    @staticmethod
    def create_directory(directory: str):
        path = Path(directory)
        if path.exists():
            FileManager._clear_directory(path)
        else:
            path.mkdir(parents=True, exist_ok=True)

    @staticmethod
    def _clear_directory(path: Path):
        for file in path.glob("*"):
            try:
                if file.is_file():
                    file.unlink()
                elif file.is_dir():
                    shutil.rmtree(file)
            except OSError as e:
                print(f"Error deleting {file}: {e}")

    @staticmethod
    def save(content: str, file_path: str):
        path = Path(file_path)
        try:
            with path.open("w", encoding="utf-8") as f:
                f.write(content)
        except IOError as e:
            print(f"Failed to save file {file_path}: {e}")
