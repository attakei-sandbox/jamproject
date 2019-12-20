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
