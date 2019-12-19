"""Core custom transforms module
"""
from typing import List, Optional
from docutils import nodes
from docutils.transforms import Transform
from janome.tokenizer import Token, Tokenizer
from . import Message, Report, TokenRepository


class Tokenize(Transform):
    """Content tokenize transform.

    At paragraph and title, tokenize internal content and bind as attribute.
    """

    default_priority = 90  # Used before other transforms of jamproject

    def apply(self):
        tokenizer = Tokenizer()  # TODO: Performance issue
        for node in self.document.traverse(nodes.paragraph):
            source = node.astext()
            node["tokens"] = TokenRepository(tokenizer.tokenize(source))


class SkillTransform(Transform):
    """Inner class to transform by skill-behavior
    """

    def __init__(self, skill_proc, skill_params, document, startnode=None):
        super().__init__(document, startnode)
        self.skill_proc = skill_proc
        self.skill_params = skill_params

    def apply(self):
        for node in self.document.traverse(nodes.paragraph):
            node.setdefault("report", Report())
            msg = self.skill_proc(node["tokens"], self.skill_params)
            if msg:
                node["report"].append(msg)
