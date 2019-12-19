"""Core custom transforms module
"""
from docutils import nodes
from docutils.transforms import Transform
from janome.tokenizer import Tokenizer


class Tokenize(Transform):
    """Content tokenize transform.

    At paragraph and title, tokenize internal content and bind as attribute.
    """

    default_priority = 90  # Used before other transforms of jamproject

    def apply(self):
        tokenizer = Tokenizer()  # TODO: Performance issue
        for node in self.document.traverse(nodes.paragraph):
            source = node.astext()
            node["tokens"] = tokenizer.tokenize(source)


class Skill(object):
    """Skill handle object class.
    """
    def __init__(self, apply, params = None):
        self.apply = apply
        """Aplly procedure for any nodes.
        """
        self.params = params

    def get_transform(self, document, startnode=None) -> Transform:
        """Transform initialization wrapper.
        """
        transform = self._Transform(document, startnode=None)
        transform._apply = self.apply
        transform._params = self.params
        return transform

    get_transform.default_priority = 400  # type: ignore

    class _Transform(Transform):
        """Inner class to transform by skill-behavior
        """
        def __init__(self, document, startnode=None):
            super().__init__(document, startnode)
            self._apply = None
            self._params = None

        def apply(self):
            for node in self.document.traverse(nodes.paragraph):
                node.setdefault("report", [])
                if self._apply is None:
                    continue
                msg = self._apply(node["tokens"], self._params)
                if msg:
                    node["report"].append(msg)
