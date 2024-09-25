import json
import os
import yt_dlp
import whisper
import requests
import click
from pathlib import Path


def download_video(url: str, output_path: str = "./downloads") -> str:
    ydl_opts = {
        "outtmpl": f"{output_path}/video.%(ext)s",
        "format": "best",
        "noplaylist": True,
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url, download=True)
        video_path = ydl.prepare_filename(info_dict)
    return video_path


def transcribe_audio(video_path: str, model_size: str = "base") -> str:
    model = whisper.load_model(model_size)
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


def summarize_text(text: str, model: str = "llama3.1") -> str:
    headers = {
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "prompt": f"請將以下逐字稿內容整理成摘要：\n\n{text}",
    }
    response = requests.post(
        "http://localhost:11434/api/generate", headers=headers, json=data
    )
    if response.status_code == 200:
        data = "".join(
            json.loads(line)["response"]
            for line in response.text.splitlines()
            if line.strip()
        )
        return data
    else:
        raise Exception(f"摘要生成失敗：{response.status_code} - {response.text}")


def save_to_file(content: str, file_path: str):
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(content)


@click.command()
@click.argument("url")
@click.option("--output", default="./output", help="摘要輸出目錄")
@click.option("--model-size", default="base", help="Whisper 模型大小")
@click.option("--ollama-model", default="llama3.1", help="Ollama 模型")
def summarize_video(url, output, model_size, ollama_model):
    """下載影片，轉錄音訊，並生成摘要。"""
    # 創建輸出目錄
    Path(output).mkdir(parents=True, exist_ok=True)

    click.echo("下載影片中...")
    try:
        video_path = download_video(url, output_path=output)
        click.echo(f"影片已下載至 {video_path}")
    except Exception as e:
        click.echo(f"下載影片失敗：{e}")
        return

    click.echo("轉錄音訊為文字中...")
    try:
        transcript = transcribe_audio(video_path, model_size=model_size)
        transcript_path = os.path.join(output, "transcript.srt")
        save_to_file(transcript, transcript_path)
        click.echo(f"轉錄文字已儲存至 {transcript_path}")
    except Exception as e:
        click.echo(f"轉錄失敗：{e}")
        return

    click.echo("生成摘要中...")
    try:
        summary = summarize_text(transcript, model=ollama_model)
        summary_path = os.path.join(output, "summary.txt")
        save_to_file(summary, summary_path)
        click.echo(f"摘要已儲存至 {summary_path}")
    except Exception as e:
        click.echo(f"生成摘要失敗：{e}")
        return

    click.echo("完成！")
