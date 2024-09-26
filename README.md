# Vdosumry

## Introduction

**Vdosumry** converts speech from videos into text and then summarizes the text.

## Prerequisites

- [ollama](https://ollama.com/): Please install ollama before installing Vdosumry

## Installation
Ensure your Python version is 3.12 or above, then install the dependencies using the following command:

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
- **--ollama-model** : Ollama model to use for summarization (default: `llama3.2`)

```bash
poetry run vdosumry "https://www.youtube.com/watch?v={youtube_youtube_id}" --output="./output" --model-size="base" --ollama-model="llama3.2"
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
