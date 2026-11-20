# Legal Sentence Game

[![Built with askThili](https://ask.thili.ai/api/v1/public/projects/wa95gypk33/badge.svg)](https://ask.thili.ai/b/wa95gypk33)

This project develops a CLI game designed for law students to practice drafting legal sentences. Players use n-gram prediction to complete partial sentences, receiving immediate feedback on the generated clause types from a fine-tuned GPT-2 model. It's an interactive way to hone legal drafting skills.

## What you are building

**Goal.** You will build a Command Line Interface (CLI) game where law students complete legal sentences using n-gram predictions, and then receive instant feedback on their completed sentences from a fine-tuned GPT-2 model.

**Done when.** The CLI game successfully presents partial legal sentences, allows the user to complete them using n-gram predictions, and then classifies the full sentence with a fine-tuned GPT-2 model, providing feedback on the generated clause types.

## Milestones

Tick these off as you go, and commit after each one.

- [ ] **1. Prepare a legal text corpus for n-gram model training.**  
      Hint: Text preprocessing and tokenization for corpus preparation.
- [ ] **2. Implement the n-gram next-word predictor.**  
      Hint: Implement n-gram probability calculation and next-word prediction logic.
- [ ] **3. Load the fine-tuned GPT-2 model for legal clause classification.**  
      Hint: Utilize the `transformers` library for loading the fine-tuned GPT-2 model.
- [ ] **4. Create a CLI game interface presenting partial legal sentences for completion.**  
      Hint: Design the command-line interface for user interaction and sentence presentation.
- [ ] **5. After user completion, classify the full sentence and provide feedback.**  
      Hint: Perform model inference on the completed sentence and display classification results.

## Run it

You need Python 3.12 and git.

```bash
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env        # then choose a model; see the comments inside
python -m app.cli hello
pytest
```

Your work goes in `app/core.py` (one stub per milestone) and `tests/test_core.py`. The first tests pass already; they
check the plumbing.

## Settings and secrets

Model settings live in `.env`, which is ignored by git. **Never commit `.env` or paste a key into code.** If a key ever
reaches GitHub, treat it as leaked and make a new one.

## Stretch ideas

- Implement a scoring system to track the user's accuracy in generating appropriate legal clause types.
- Offer multiple-choice options for the next word, generated from the n-gram model's top predictions.
- Allow users to select different difficulty levels, perhaps by varying the length of the partial sentences provided.
