import pytest
from docutils import nodes
from docutils.core import publish_doctree
from docutils.readers import Reader
from jamproject.transforms import Tokenize


class TokenizeOnlyReader(Reader):
    def get_transforms(self):
        return super().get_transforms() + [Tokenize]


@pytest.mark.parametrize("source,tokens_size", [("本日は晴天なり", 4), ("毎日が日曜日", 3),])
def test_single_text_tokenize(source, tokens_size):
    doctree = publish_doctree(source, reader=TokenizeOnlyReader())
    paragraph: nodes.paragraph = doctree.children[0]
    assert "tokens" in paragraph.attributes
    tokens = paragraph.attributes["tokens"]
    assert len(tokens) == tokens_size
