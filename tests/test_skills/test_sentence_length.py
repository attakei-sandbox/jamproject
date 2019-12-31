from dataclasses import dataclass
from motto.core import TokenRepository
from motto.skills.sentence_length import Skill


@dataclass
class Token(object):
    surface: str


def test_regular():
    skill = Skill()
    # 5 letters
    tokens = TokenRepository([Token("sample")])
    assert skill.proc(tokens, {}) is None


def test_long_strings():
    skill = Skill()
    # 120 letters
    tokens = TokenRepository([Token("sample" * 20)])
    assert skill.proc(tokens, {}) is not None
    msg = skill.proc(tokens, {})
    assert "actually: 120" in msg.body


def test_include_spacings():
    skill = Skill()
    # 77 letters with 6 spaces
    tokens = TokenRepository([Token("example" * 11)] + [Token("      ")])
    assert skill.proc(tokens, {}) is None
