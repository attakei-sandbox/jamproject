import pytest
from dataclasses import dataclass
from motto.tokenizers import _slice_tokens, split_tokens


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


@pytest.mark.parametrize(
    "text,s_cnt",
    [
        (["こんにちは"], 1),
        (["こんにちは", "。"], 1),
        (["ありがとう", "。", "さようなら"], 2),
        (["ありがとう", "。", "さようなら", "。", "では"], 3),
    ],
)
def test_split_tokens__patterns(text, s_cnt):
    tokens = [Token(t) for t in text]
    splitted = split_tokens(tokens, ["。"])
    assert len(splitted) == s_cnt


@pytest.mark.parametrize(
    "text,delimiters,s_cnt",
    [
        (["ありがとう", "。", "さようなら"], ["."], 1),
        (["ありがとう", "。", "さようなら"], ["。"], 2),
        (["ありがとう", "。", "さようなら"], None, 2),
    ],
)
def test_split_tokens__delimter_patterns(text, delimiters, s_cnt):
    tokens = [Token(t) for t in text]
    splitted = split_tokens(tokens, delimiters)
    assert len(splitted) == s_cnt
