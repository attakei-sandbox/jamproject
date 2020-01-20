from dataclasses import dataclass
from motto.core import Sentence
from motto.skills.sentence_length import Skill


@dataclass
class Token(object):
    surface: str


def test_regular():
    skill = Skill()
    # 5 letters
    sentences = Sentence([Token("sample")])
    assert skill.proc(sentences, {}) is None


def test_long_strings():
    skill = Skill()
    # 120 letters
    sentences = Sentence([Token("sample" * 20)])
    assert skill.proc(sentences, {}) is not None
    msg = skill.proc(sentences, {})
    assert "actually: 120" in msg.body


def test_include_spacings():
    skill = Skill()
    # 77 letters with 6 spaces
    sentences = Sentence([Token("example" * 11)] + [Token("      ")])
    assert skill.proc(sentences, {}) is None
