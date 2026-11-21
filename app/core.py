"""Legal Sentence Game: one small function per milestone."""
import random
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


# --- Milestone 3: load the model
def milestone_3():
    from app.llm import load_gpt2
    return load_gpt2()


# --- Milestone 5: classify the finished sentence
def milestone_5(sentence):
    from app.llm import classify
    return classify(sentence)


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