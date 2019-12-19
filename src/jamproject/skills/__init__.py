from typing import List
from docutils.transforms import Transform
from janome.tokenizer import Token
from ..core.transforms import SkillTransform


class SkillBase(object):
    """Skill handle object class.
    """
    default_priority = 400

    def __init__(self, params=None):
        self.params = params

    def apply(self, tokens: List[Token], params):
        raise NotImplementedError()

    def __call__(self, document, startnode=None) -> Transform:
        """Transform initialization wrapper.
        """
        return SkillTransform(self.apply, self.params, document, startnode=None)
