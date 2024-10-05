import os
import gettext
import click
from vdosumry import (
    VideoDownloader,
    AudioTranscriber,
    TextSummarizer,
    FileManager,
    TextTranslator,
)
from .llm.ollama import Ollama

# Set up gettext
localedir = os.path.join(os.path.abspath(os.path.dirname(__file__)), "..", "locales")
lang = os.environ.get("LANG", "en").split(".")[0]
translation = gettext.translation(
    "vdosumry", localedir, languages=[lang], fallback=True
)
translation.install()
_ = translation.gettext


@click.command()
@click.argument("url")
@click.option("--output", default="./output", help=_("Directory to save the summary"))
@click.option("--model-size", default="base", help=_("Size of the Whisper model"))
@click.option(
    "--ollama-model",
    default="llama3.2",
    help=_("Ollama model to use for summarization"),
)
@click.option("--language", default="zh-TW", help=_("Summarization language"))
def summarize_video(url, output, model_size, ollama_model, language):
    """Download video, transcribe audio, and generate summary."""
    FileManager.create_directory(output)

    downloader = VideoDownloader(output_path=output)
    transcriber = AudioTranscriber(model_size=model_size)
    ollama = Ollama(model=ollama_model)

    click.echo(_("Downloading video..."))
    try:
        video_path = downloader.download(url)
        click.echo(_("Video downloaded to {}").format(video_path))
    except Exception as e:
        click.echo(_("Failed to download video: {}").format(e))
        return

    click.echo(_("Transcribing audio to text..."))
    try:
        transcriber.transcribe(video_path)
        transcript_path = os.path.join(output, "transcript.srt")
        FileManager.save(transcriber.get_srt_format(), transcript_path)
        click.echo(_("Transcript saved to {}").format(transcript_path))
    except Exception as e:
        click.echo(_("Failed to transcribe: {}").format(e))
        return

    click.echo(_("Generating summary..."))
    try:
        summarizer = TextSummarizer(llm=ollama)
        summary = summarizer.summarize(transcriber.get_text_format())
        summary_path = os.path.join(output, "summary.txt")
        FileManager.save(summary, summary_path)
        click.echo(_("Summary saved to {}").format(summary_path))
    except Exception as e:
        click.echo(_("Failed to generate summary: {}").format(e))
        return

    click.echo(_("Translating summary..."))
    try:
        translator = TextTranslator(target_language=language, llm=ollama)
        translate_summary = translator.translate(summary)
        translate_path = os.path.join(output, "translate.txt")
        FileManager.save(translate_summary, translate_path)
        click.echo(_("Translated summary saved to {}").format(translate_path))
    except Exception as e:
        click.echo(_("Failed to translate summary: {}").format(e))
        return

    click.echo(_("Done!"))
