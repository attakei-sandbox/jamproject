"""Core classes for jamproject
"""
from typing import ClassVar, List, Protocol, Tuple, Union


class Message(object):
    """Reporting message class.

    This object is appended for paragraphes by skills.
    Responsibility is only telling event "what" for user, not "where".
    """

    def __init__(self, body: str):
        self.body: str = body
        """message body"""


class Report(object):
    """Report by skills.
    """

    def __init__(self):
        self._messages: List[Message] = []

    def __repr__(self):
        cnt = len(self)
        if cnt == 0:
            return "[No reports]"
        if cnt == 1:
            return "[1 report]"
        return f"[{cnt} reports]"

    def __len__(self) -> int:
        return len(self._messages)


class Token(Protocol):
    surface: ClassVar[str]


class TokenRepository(object):
    """Token dataset and accessor.
    """

    def __init__(self, tokens: Union[Tuple[Token, ...], List[Token]]):
        self._tokens: Tuple[Token, ...] = tuple(tokens) if isinstance(
            tokens, list
        ) else tokens

    def __repr__(self) -> str:
        cnt = len(self)
        if cnt == 0:
            return "[no tokens]"
        if cnt == 1:
            return "[1 token]"
        return f"[{cnt} tokens]"

    def __len__(self) -> int:
        return len(self._tokens)

    def __getitem__(self, key) -> Token:
        return self._tokens[key]
