import app.llm
from app.core import milestone_1, milestone_2, milestone_3, milestone_4, milestone_5


def test_milestone_1_corpus_is_tokenized():
    sentences = milestone_1()
    assert len(sentences) > 0
    assert all(isinstance(w, str) for w in sentences[0])


def test_milestone_2_next_word():
    assert milestone_2("either") == "party"
    assert milestone_2("zzzz") is None


def test_milestone_3_loads_model(monkeypatch):
    monkeypatch.setattr(app.llm, "load_gpt2", lambda: "fake-model")
    assert milestone_3() == "fake-model"


def test_milestone_5_classifies(monkeypatch):
    monkeypatch.setattr(app.llm, "classify", lambda s: "Termination")
    assert milestone_5("either party may terminate") == "Termination"


def test_milestone_4_game_flow(monkeypatch, capsys):
    answers = iter(["terminate", ""])
    monkeypatch.setattr("builtins.input", lambda _: next(answers))
    monkeypatch.setattr(app.llm, "classify", lambda s: "Termination")
    milestone_4()
    assert "Clause type: Termination" in capsys.readouterr().out