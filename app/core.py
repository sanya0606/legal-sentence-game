"""Legal Sentence Game: one small function per milestone."""
import os, random
from collections import Counter, defaultdict

CORPUS = [
    "This agreement shall be governed by the laws of the State of New York.",
    "The party shall indemnify and hold harmless the other party from all claims.",
    "Either party may terminate this agreement upon thirty days written notice.",
    "All information disclosed shall be kept strictly confidential by the receiving party.",
    "This agreement constitutes the entire agreement between the parties.",
    "Any notice required under this agreement shall be given in writing.",
]


# --- Milestone 1: prepare the corpus (lowercase, split into words)
def milestone_1():
    return [s.lower().replace(".", " .").split() for s in CORPUS]


# --- Milestone 2: bigram next-word predictor
def milestone_2(prev_word=None, sentences=None):
    sentences = sentences or milestone_1()
    nxt = defaultdict(Counter)
    for s in sentences:
        for a, b in zip(s, s[1:]):
            nxt[a][b] += 1
    if prev_word is None:                      # no word yet: return the model
        return nxt
    counts = nxt.get(prev_word.lower())
    return counts.most_common(1)[0][0] if counts else None


# --- Milestone 3: load the fine-tuned GPT-2 (folder from your LEDGAR drill)
def milestone_3():
    from transformers import AutoTokenizer, AutoModelForCausalLM
    path = os.getenv("MODEL_DIR", "gpt2-ledgar")
    return AutoTokenizer.from_pretrained(path), AutoModelForCausalLM.from_pretrained(path)


# --- Milestone 5: classify the finished sentence (label = next token)
def milestone_5(sentence, tok_model=None):
    tok, model = tok_model or milestone_3()
    ids = tok(sentence, return_tensors="pt")
    out = model.generate(**ids, max_new_tokens=1, do_sample=False,
                         pad_token_id=tok.eos_token_id)
    return tok.decode(out[0, -1]).strip()


# --- Milestone 4: the CLI game (calls milestones 2 and 5)
def milestone_4():
    sentences = milestone_1()
    words = random.choice(sentences)[:3]
    print("Complete the legal sentence. Press Enter on a blank line when done.")
    while True:
        print("\n" + " ".join(words))
        hint = milestone_2(words[-1])
        w = input(f"next word (hint: {hint}): ").strip()
        if not w:
            break
        words.append(w)
    sentence = " ".join(words)
    print("\nYour sentence:", sentence)
    print("Clause type:", milestone_5(sentence))