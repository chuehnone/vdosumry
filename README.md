# Vdosumry

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="README-zh-TW.md"><img alt="繁體中文文件" src="https://img.shields.io/badge/繁體中文-d9d9d9"></a>
</p>

## Introduction

**Vdosumry** converts speech from videos into text and then summarizes the text.

## Prerequisites

- [ollama](https://ollama.com/): Please install ollama before installing Vdosumry
- [ffmpeg](https://ffmpeg.org/): Please install ffmpeg before installing Vdosumry
  - macOS: `brew install ffmpeg`
- [llvm@14](https://releases.llvm.org/): Please install llvm before installing Vdosumry
  - macOS: `brew install llvm@14`
- [poetry](https://python-poetry.org/): Please install poetry before installing Vdosumry
  - macOS: `brew install poetry`

## Installation
Ensure your Python version is 3.11 or above, then install the dependencies using the following command:

```bash
poetry install
```

## Usage

To generate a summary of a video, run the following command:

```bash
poetry run vdosumry https://www.youtube.com/watch\?v={youtube_youtube_id}
```

or 

```bash
poetry run vdosumry "https://www.youtube.com/watch?v={youtube_youtube_id}"
```

### Command Options

- **--output** : Directory to save the summary (default: `./output`)
- **--model-size** : Size of the Whisper model (default: `base`)
- **--ollama-model** : Ollama model to use for summarization (default: select first local available ollama model)
- **--language** : summarization language (default: `zh-TW`)

```bash
poetry run vdosumry "https://www.youtube.com/watch?v={youtube_youtube_id}" --output="./output" \
--model-size="base" --ollama-model="llama3.2" --language="zh-TW"
```

## Contribution

Issues and pull requests are welcome. Please ensure your code adheres to the project's coding standards.

### Linter

Use Ruff to lint your code before opening a pull request.

```bash
poetry run ruff format
``` 

## License
This project is licensed under the MIT License.
