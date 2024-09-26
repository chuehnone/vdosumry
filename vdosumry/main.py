import os
import click
from pathlib import Path
from vdosumry.video_downloader import VideoDownloader
from vdosumry.audio_transcriber import AudioTranscriber
from vdosumry.text_summarizer import TextSummarizer
from vdosumry.file_manager import FileManager


@click.command()
@click.argument("url")
@click.option("--output", default="./output", help="摘要輸出目錄")
@click.option("--model-size", default="base", help="Whisper 模型大小")
@click.option("--ollama-model", default="llama3.1", help="Ollama 模型")
def summarize_video(url, output, model_size, ollama_model):
    """下載影片，轉錄音訊，並生成摘要。"""
    # 創建輸出目錄
    Path(output).mkdir(parents=True, exist_ok=True)

    downloader = VideoDownloader(output_path=output)
    transcriber = AudioTranscriber(model_size=model_size)
    summarizer = TextSummarizer(model=ollama_model)
    file_manager = FileManager()

    click.echo("下載影片中...")
    try:
        video_path = downloader.download(url)
        click.echo(f"影片已下載至 {video_path}")
    except Exception as e:
        click.echo(f"下載影片失敗：{e}")
        return

    click.echo("轉錄音訊為文字中...")
    try:
        transcript = transcriber.transcribe(video_path)
        transcript_path = os.path.join(output, "transcript.srt")
        file_manager.save(transcript, transcript_path)
        click.echo(f"轉錄文字已儲存至 {transcript_path}")
    except Exception as e:
        click.echo(f"轉錄失敗：{e}")
        return

    click.echo("生成摘要中...")
    try:
        summary = summarizer.summarize(transcript)
        summary_path = os.path.join(output, "summary.txt")
        file_manager.save(summary, summary_path)
        click.echo(f"摘要已儲存至 {summary_path}")
    except Exception as e:
        click.echo(f"生成摘要失敗：{e}")
        return

    click.echo("完成！")
