import configparser
import pytest
from pathlib import Path
from jamproject.config import find_filepath


here = Path(__file__).parent.resolve()


@pytest.mark.parametrize(
    "targets,filename",
    [
        ([".jamproject.ini"], ".jamproject.ini"),
        ([".jamproject.ini", "setup.cfg"], ".jamproject.ini"),
        (["setup.cfg", ".jamproject.ini"], "setup.cfg"),
    ],
)
def test_collect_all_sources(targets, filename):
    config_path: Path = find_filepath(here / "test_config", targets)
    assert config_path.name == filename
