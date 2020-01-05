import pytest
from dataclasses import dataclass
from motto.core.tokenizers import _slice_tokens


@dataclass
class Token(object):
    surface: str


@pytest.mark.parametrize(
    "text,s_cnt,r_cnt",
    [(["こんにちは"], 1, 0), (["こんにちは", "。"], 2, 0), (["ありがとう", "。", "さようなら"], 2, 1),],
)
def test__slice_tokens__patterns(text, s_cnt, r_cnt):
    tokens = [Token(t) for t in text]
    splitted, remained = _slice_tokens(tokens, ["。"])
    assert len(splitted) == s_cnt
    assert len(remained) == r_cnt
