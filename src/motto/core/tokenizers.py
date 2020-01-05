from typing import Iterable, List, Sized, Text, Tuple, Union
from . import Token


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
