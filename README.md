# Legal Sentence Game

A command-line game where law students complete a partial legal sentence one word at a time, with next-word hints from an n-gram model. At the end, a language model classifies the sentence into a clause type (e.g. Termination, Governing_Law).

## How it works
- **Corpus:** 6 hand-written legal sentences in `app/core.py` (no external dataset).
- **Next word:** a bigram model that suggests the most common word that follows the last one.
- **Classification:** an LLM called through Groq (configured in `.env`) returns the clause type.
- **History:** every sentence you play is saved with its clause type in `data/app.json` (via `app/storage.py`).

## Run it
```
python3.12 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
```
Edit `.env` and set `LLM_BASE_URL`, `LLM_API_KEY` and `LLM_MODEL` (a free Groq key works).
```
python -m app.cli
pytest
```

## Example output
```
Legal Sentence Game is ready.
Complete the legal sentence. Press Enter on a blank line when done.

all information disclosed
next word (hint: shall): shall

all information disclosed shall
next word (hint: be): be

all information disclosed shall be
next word (hint: governed): governed

all information disclosed shall be governed
next word (hint: by): by

all information disclosed shall be governed by
next word (hint: the): the

all information disclosed shall be governed by the
next word (hint: laws): laws

all information disclosed shall be governed by the laws
next word (hint: of): of

all information disclosed shall be governed by the laws of
next word (hint: the): the

all information disclosed shall be governed by the laws of the
next word (hint: laws): laws

all information disclosed shall be governed by the laws of the laws
next word (hint: of): 

Your sentence: all information disclosed shall be governed by the laws of the laws
Clause type: Governing_Law

## Baseline and limits
- The n-gram model only knows 6 sentences, so hints repeat a lot and are empty for unseen words.
- Classification was checked by hand on a few sentences, not on a labelled test set, so accuracy is unmeasured.
- Clause types come from a general LLM, not a GPT-2 model fine-tuned in this project.