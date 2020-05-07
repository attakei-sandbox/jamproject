from unittest import mock
from docutils import nodes
from docutils.core import publish_doctree
from motto.core.base import SkillBase
from motto.readers import Reader


class Skill(SkillBase):
    mocked = mock.Mock(side_effect=None)

    def proc(self, tokens, params):
        self.mocked()


def test_skill_called():
    skill = Skill(None)
    reader = Reader()
    reader.add_skill(skill)
    doctree = publish_doctree("本日は晴天なり", reader=reader)
    paragraph: nodes.paragraph = doctree.children[0]
    assert skill.mocked.called
