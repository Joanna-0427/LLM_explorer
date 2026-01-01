# LLM Explorer (CLI)

A lightweight command-line tool to:
- Generate short completions with OpenAI models
- Compare outputs across multiple models
- Inspect tokenization with `tiktoken`
- Count tokens for a given input text

This repo is intentionally minimal and focused on experimentation.

---

## Features

- **Generate text**: Provide a prompt and get a short completion (configured to keep output concise).
- **Model comparison**: Run the same prompt across multiple models and print outputs side-by-side.
- **Tokenize text**: Convert text into token IDs using `tiktoken`.
- **Token counting**: Count the number of tokens for a given text.

---

## Requirements

- Python 3.9+ recommended
- An OpenAI API key
- Python packages:
  - `openai`
  - `tiktoken`

---

## Setup

### 1) Create and activate a virtual environment (recommended)

```bash
python -m venv .venv
source .venv/bin/activate  # macOS/Linux
# .venv\Scripts\activate   # Windows PowerShell

2) Install dependencies
pip install openai tiktoken


3) Set your OpenAI API key

macOS/Linux:

export OPENAI_API_KEY="YOUR_API_KEY"


Windows (PowerShell):

setx OPENAI_API_KEY "YOUR_API_KEY"


# LLM Explorer

A lightweight CLI tool for experimenting with LLM outputs and tokenization.

## Run

```bash
python LLM_explorer.py
---
## Run
‘’‘python LLM_explorer.py

---

## Exit

---

##Configuration

In LLM_explorer.py, the script defines:

models: the model list used for comparison, e.g.

models = ["gpt-3.5-turbo", "gpt-4o-mini"]


generate_text(prompt): uses client.responses.create(...) with a short-output instruction.

model_comparison(prompt, models): loops through the models and prints each completion.

tiktoken_show(text) / tiktoken_count(text): tokenizes and counts tokens for the given text.

You can adjust:

-temperature

-max_output_tokens

-models list

---

#Known Issues / Quick Fix
tiktoken fallback function name

If you see an error around get_coding, update:

encoding = tiktoken.get_coding("cl100k_base")


to:

encoding = tiktoken.get_encoding("cl100k_base")


This matches the standard tiktoken API.

---

##Notes

The script sends requests to OpenAI; usage may incur API costs depending on your account and model.

Avoid putting secrets (API keys) directly into code. Use environment variables instead.

License

Add a license if you plan to share this project publicly.
