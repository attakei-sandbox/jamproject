from pathlib import Path
from jamproject.core import config


here = Path(__file__).parent.resolve()
testdata_dir = here / "test_config"


def test_parse_cfg():
    path = testdata_dir / "no-config.cfg"
    cfg = config._parse_config(path)
    assert "skills" in cfg


def test_parse_cfg_1():
    path = testdata_dir / "has-skill.cfg"
    cfg = config._parse_config(path)
    assert "sentence_length" in cfg["skills"]


def test_no_config():
    path = testdata_dir / "no-config.cfg"
    cfg = config.load_config(path, {})
    assert cfg == {}


def test_no_config_override():
    path = testdata_dir / "has-skill.cfg"
    cfg = config.load_config(path, {})
    assert "sentence_length" in cfg["skills"]


def test_default_skills():
    path = testdata_dir / "no-config.cfg"
    cfg = config.load_config(path)
    assert cfg["skills"] != {}
