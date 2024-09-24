# Vdosumry

## Introduction

**Vdosumry** converts speech from videos into text and then summarizes the text.

## Prerequisites

- ollama

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

## Contribution
Issues and pull requests are welcome. Please ensure your code adheres to the project's coding standards.

## License
This project is licensed under the MIT License.
