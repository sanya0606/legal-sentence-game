"""LLM helpers: chat() for Ollama/Groq/Gemini, classify() for GPT-2 or chat fallback."""
import os
from pathlib import Path

import httpx


def _load_env() -> None:
    """Read KEY=VALUE lines from .env (if there is one) without overriding real environment variables."""
    path = Path(".env")
    if not path.exists():
        return
    for line in path.read_text().splitlines():
        line = line.strip()
        if line and not line.startswith("#") and "=" in line:
            key, value = line.split("=", 1)
            os.environ.setdefault(key.strip(), value.strip())


def settings() -> tuple[str, str, str]:
    _load_env()
    return (os.environ.get("LLM_BASE_URL") or "http://localhost:11434/v1",
            os.environ.get("LLM_API_KEY", ""), os.environ.get("LLM_MODEL", ""))


def chat(messages: list[dict], **options) -> str:
    """Send chat messages, get the reply text. `options` go straight to the API (temperature, max_tokens...)."""
    base, key, model = settings()
    if not model:
        raise RuntimeError("Set LLM_MODEL in .env (see .env.example).")
    headers = {"Authorization": f"Bearer {key}"} if key else {}
    r = httpx.post(f"{base.rstrip('/')}/chat/completions", headers=headers, timeout=120,
                   json={"model": model, "messages": messages, **options})
    r.raise_for_status()
    return r.json()["choices"][0]["message"]["content"]
_gpt2 = None  # loaded once, reused


def load_gpt2():
    """Load the fine-tuned GPT-2 from MODEL_DIR (milestone 3)."""
    global _gpt2
    if _gpt2 is None:
        from transformers import AutoTokenizer, AutoModelForCausalLM
        path = os.environ["MODEL_DIR"]
        _gpt2 = (AutoTokenizer.from_pretrained(path),
                 AutoModelForCausalLM.from_pretrained(path))
    return _gpt2


def classify(sentence: str) -> str:
    """Return the clause type of a sentence (milestone 5)."""
    _load_env()
    if os.environ.get("MODEL_DIR"):
        tok, model = load_gpt2()
        ids = tok(sentence, return_tensors="pt")
        out = model.generate(**ids, max_new_tokens=1, do_sample=False,
                             pad_token_id=tok.eos_token_id)
        return tok.decode(out[0, -1]).strip()
    return chat([
        {"role": "system", "content": "You classify legal clauses. Reply with only the clause type, "
                                      "e.g. Governing_Law, Indemnity, Termination, Confidentiality, Notices."},
        {"role": "user", "content": sentence},
    ], temperature=0).strip()