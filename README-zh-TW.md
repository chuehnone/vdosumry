# Vdosumry

<p align="center">
  <a href="./README.md"><img alt="README in English" src="https://img.shields.io/badge/English-d9d9d9"></a>
  <a href="README-zh-TW.md"><img alt="繁體中文文件" src="https://img.shields.io/badge/繁體中文-d9d9d9"></a>
</p>

## 簡介

**Vdosumry** 能夠將線上影片中的語音轉換成文字，並對文字進行摘要。

## 前期準備

- [ollama](https://ollama.com/): 需要在本地端安裝 ollama 才能使用 Vdosumry
- [ffmpeg](https://ffmpeg.org/): 需要在本地端安裝 ffmpeg 才能安裝 Vdosumry
  - macOS: `brew install ffmpeg`
- [llvm@14](https://releases.llvm.org/): 需要在本地端安裝 llvm@14 才能安裝 Vdosumry
  - macOS: `brew install llvm@14`
- [poetry](https://python-poetry.org/): 需要在本地端安裝 poetry 才能安裝 Vdosumry
  - macOS: `brew install poetry`

## 安裝
確認您的本地端 python 版本是 3.11 或更新的版本。

```bash
poetry install
```

## 使用方法

要生成影片摘要，請執行以下命令：

```bash
poetry run vdosumry https://www.youtube.com/watch\?v={youtube_youtube_id}
```

or 

```bash
poetry run vdosumry "https://www.youtube.com/watch?v={youtube_youtube_id}"
```

### 指令選項

- **--output** : 檔案輸出的資料夾位置 (預設: `./output`)
- **--model-size** : Whisper 模型 (預設: `base`)
- **--ollama-model** : Ollama 模型 (預設: `llama3.2`)
- **--language** : 摘要的語言 (預設: `zh-TW`)

```bash
poetry run vdosumry "https://www.youtube.com/watch?v={youtube_youtube_id}" --output="./output" \
--model-size="base" --ollama-model="llama3.2" --language="zh-TW"
```

## Contribution

歡迎提出 Issues 或 Pull Requests。請確保您的程式碼有通過 Linter 標準。

### Linter

在開啟 Pull Requests 之前，使用 Ruff 檢查您的程式碼。

```bash
poetry run ruff format
``` 

## License

此專案採用 MIT 授權條款。
