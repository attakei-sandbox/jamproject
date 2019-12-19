"""Core classes for jamproject
"""


class Message(object):
    """Reporting message class.

    This object is appended for paragraphes by skills.
    Responsibility is only telling event "what" for user, not "where".
    """

    def __init__(self, body: str):
        self.body: str = body
        """message body"""


class Report(object):
    def __init__(self):
        self.messages = []

    def __repr__(self):
        msgs = len(self.messages)
        if msgs == 0:
            return "[No reports]"
        if msgs == 1:
            return "[1 report]"
        return f"[{msgs} reports]"

    def has_message(self):
        return len(self.messages) > 0

    def append(self, msg: Message):
        self.messages.append(msg)


class TokenRepository(object):
    def __init__(self, tokens: tuple):
        self.items = tokens

    def __repr__(self):
        tokens = len(self.items)
        if tokens == 1:
            return "[1 token]"
        return f"[{tokens} tokens]"
