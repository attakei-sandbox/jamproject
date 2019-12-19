import pytest
from textwrap import dedent
from docutils import nodes
from docutils.core import publish_doctree
from docutils.readers import Reader
from jamproject.transforms import Tokenize
from jamproject.skills.sentence_length import Skill


class TokenizeOnlyReader(Reader):
    def get_transforms(self):
        return super().get_transforms() + [Tokenize, Skill()]


def test_safe():
    doctree = publish_doctree("本日は晴天なり", reader=TokenizeOnlyReader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 0


def test_failure():
    doctree = publish_doctree("本日は晴天なり" * 20, reader=TokenizeOnlyReader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 1
    assert "80" in report[0].body
    assert "140" in report[0].body


def test_safe_parameterized():
    skill = Skill({"max": 140})

    class CustomReader(Reader):
        def get_transforms(self):
            return super().get_transforms() + [Tokenize, skill]

    doctree = publish_doctree("本日は晴天なり" * 20, reader=CustomReader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 0
