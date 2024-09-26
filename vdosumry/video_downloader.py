import yt_dlp

class VideoDownloader:
    def __init__(self, output_path="./downloads"):
        self.output_path = output_path

    def download(self, url: str) -> str:
        ydl_opts = {
            "outtmpl": f"{self.output_path}/video.%(ext)s",
            "format": "best",
            "noplaylist": True,
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(url, download=True)
            video_path = ydl.prepare_filename(info_dict)
        return video_path