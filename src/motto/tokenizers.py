from typing import Iterable, List, Optional, Sized, Text, Tuple, Union
from .core import Sentence, Token


DEFAULT_DELIMITERS = [".", "。"]

Tokens = Union[List[Token], Tuple[Token, ...]]

SplitResult = Tuple[Tokens, Tokens]


def _slice_tokens(tokens: Tokens, delimiters: Iterable[Text]) -> SplitResult:
    """Slice tokens once by delimter.

    :param tokens: Token sequence
    :param delimiters: Delimieter patterns lise
    :returns: Sliced tokens(include delimiter)
    """
    pos = len(tokens)
    for pos, t in enumerate(tokens, 1):
        if t.surface in delimiters:
            break
    return tokens[:pos], tokens[pos:]


def split_tokens(
    tokens: Tokens, delimiters: Optional[Iterable[Text]] = None
) -> List[Sentence]:
    """
    :param tokens: Source tokens
    :param delemiters: Delimiter patterns list
    :returns: Full-splitted tokens as Sentence list
    """
    if not delimiters:
        delimiters = DEFAULT_DELIMITERS
    splitted = []
    remains = tokens
    while len(remains) > 0:
        s, r = _slice_tokens(remains, delimiters)
        splitted.append(s)
        remains = r
    return [Sentence(t) for t in splitted]
