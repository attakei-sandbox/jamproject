import importlib
from typing import List, Optional
from .core import Config, Message, Sentence, SkillParams
from .transforms import SkillTransform


class SkillBase(object):
    """Base class of motto-skills.
    """

    default_priority = 400

    def __init__(self, params: Optional[SkillParams] = None):
        self.params = params if params is not None else {}

    def __call__(self, document, startnode=None) -> SkillTransform:
        return SkillTransform(self.proc, self.params, document, startnode)

    def proc(self, tokens: Sentence, params: SkillParams) -> Optional[Message]:
        """Skill implementation for tokens.
        """
        raise NotImplementedError()


def load_skills(config: Config) -> List[SkillBase]:
    skills = []
    for k, param in config["skills"].items():
        module = importlib.import_module(param["module"])
        if hasattr(module, "Skill"):
            skill = getattr(module, "Skill")(param)
            skills.append(skill)
    return skills
