import os

import click
from vdosumry import (
    VideoDownloader,
    AudioTranscriber,
    TextSummarizer,
    FileManager,
    TextTranslator,
)
from .llm.ollama import Ollama


@click.command()
@click.argument("url")
@click.option("--output", default="./output", help="摘要輸出目錄")
@click.option("--model-size", default="base", help="Whisper 模型大小")
@click.option("--ollama-model", default="llama3.2", help="Ollama 模型")
@click.option("--language", default="zh-TW", help="指定輸出的摘要語言")
def summarize_video(url, output, model_size, ollama_model, language):
    """下載影片，轉錄音訊，並生成摘要。"""
    # Create output directory if not exists or clear the directory if exists
    FileManager.create_directory(output)

    downloader = VideoDownloader(output_path=output)
    transcriber = AudioTranscriber(model_size=model_size)
    ollama = Ollama(model=ollama_model)

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
        FileManager.save(transcript, transcript_path)
        click.echo(f"轉錄文字已儲存至 {transcript_path}")
    except Exception as e:
        click.echo(f"轉錄失敗：{e}")
        return

    click.echo("生成摘要中...")
    try:
        summarizer = TextSummarizer(llm=ollama)
        summary = summarizer.summarize(transcript)
        summary_path = os.path.join(output, "summary.txt")
        FileManager.save(summary, summary_path)
        click.echo(f"摘要已儲存至 {summary_path}")
    except Exception as e:
        click.echo(f"生成摘要失敗：{e}")
        return

    click.echo("摘要翻譯中...")
    try:
        translator = TextTranslator(target_language=language, llm=ollama)
        translate_summary = translator.translate(summary)
        translate_path = os.path.join(output, "translate.txt")
        FileManager.save(translate_summary, translate_path)
        click.echo(f"摘要翻譯已儲存至 {translate_path}")
    except Exception as e:
        click.echo(f"摘要翻譯失敗：{e}")
        return

    click.echo("完成！")
