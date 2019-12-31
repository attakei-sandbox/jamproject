"""This skill-module add report already
"""
from jamproject.core import Message
from jamproject.core.base import SkillBase


class Skill(SkillBase):
    def proc(self, tokens, params):
        return Message("This skill is regnsted.")
