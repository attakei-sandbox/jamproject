import pytest
from textwrap import dedent
from docutils import nodes
from docutils.core import publish_doctree
from motto import readers


@pytest.mark.parametrize("source,tokens_size", [("本日は晴天なり", 4), ("毎日が日曜日", 3)])
def test_single_text_tokenize(source, tokens_size):
    doctree = publish_doctree(source, reader=readers.Reader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "sentences" in paragraph.attributes
    assert "report" in paragraph.attributes
    sentences = paragraph.attributes["sentences"]
    assert len(sentences[0]) == tokens_size


@pytest.mark.parametrize("source,sentence_num", [("本日は晴天なり。毎日が日曜日", 2)])
def test_multiple_text_tokenize(source, sentence_num):
    doctree = publish_doctree(source, reader=readers.Reader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "sentences" in paragraph.attributes
    sentences = paragraph.attributes["sentences"]
    assert len(sentences) == sentence_num


def test_tokenize_url_reference():
    source = "`ここ <http://example.com>`_"
    doctree = publish_doctree(source, reader=readers.Reader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "sentences" in paragraph.attributes
    assert "report" in paragraph.attributes
    sentences = paragraph.attributes["sentences"]
    assert len(sentences) == 1
    assert sentences[0][0].surface == "ここ"


def test_tokenize_multiline():
    source = """
    本日は晴天なり、
    という会話。
    """
    source = dedent(source).strip()
    doctree = publish_doctree(source, reader=readers.Reader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "sentences" in paragraph.attributes
    assert "report" in paragraph.attributes
    sentences = paragraph.attributes["sentences"]
    assert len(sentences[0]) == 9
