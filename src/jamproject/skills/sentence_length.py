"""Skill of jamproject: Check length of sentence
"""
from typing import List, Optional
from janome.tokenizer import Token
from ..core import Message


def count_length(tokens: List[Token]) -> int:
    return sum([len(t.surface) for t in tokens])


def apply(tokens: List[Token]) -> Optional[Message]:
    length = count_length(tokens)
    msg = f"{__name__}, expected: {80}, actually: {length}"
    return Message(msg) if length > 80 else None
