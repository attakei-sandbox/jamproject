import pytest
from textwrap import dedent
from docutils import nodes
from docutils.core import publish_doctree
from jamproject.core.readers import Reader
from jamproject.core.transforms import Tokenize
from jamproject.skills.sentence_length import Skill


def test_safe():
    reader = Reader()
    reader.skills = [Skill()]
    doctree = publish_doctree("本日は晴天なり", reader=reader)
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 0


def test_failure():
    reader = Reader()
    reader.skills = [Skill()]
    doctree = publish_doctree("本日は晴天なり" * 20, reader=reader)
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 1
    assert "80" in report[0].body
    assert "140" in report[0].body


def test_safe_parameterized():
    reader = Reader()
    reader.skills = [Skill({"max": 140})]
    doctree = publish_doctree("本日は晴天なり" * 20, reader=reader)
    paragraph: nodes.paragraph = doctree.children[0]
    assert "report" in paragraph.attributes
    report = paragraph.attributes["report"]
    assert len(report) == 0
