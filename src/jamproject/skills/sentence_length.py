"""Skill of jamproject: Check length of sentence
"""
from typing import Any, Dict, List, Optional
from janome.tokenizer import Token
from ..core import Message
from ..core.transforms import SkillBase


default_config = {
    "max": 80,
}


def count_length(tokens: List[Token]) -> int:
    return sum([len(t.surface) for t in tokens])


class Skill(SkillBase):
    def apply(self, tokens: List[Token], params: Optional[Dict[str, Any]]) -> Optional[Message]:
        params = {} if params is None else params
        length = count_length(tokens)
        max_length = params.get("max", default_config["max"])
        msg = f"{__name__}, expected: {max_length}, actually: {length}"
        return Message(msg) if length > max_length else None
