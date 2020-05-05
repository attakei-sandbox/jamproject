import pytest
from pathlib import Path
from motto.core import path

here = Path(__file__).parent.resolve()


@pytest.mark.parametrize("ext,expect", [(None, 13), ("py", 5)])
def test_collect_files__case_ext(ext, expect):
    files = path.collect_files([here], ext=ext)
    assert len(files) == expect


def test_collect_files__multilpe_files():
    files = path.collect_files([here / "test_config.py", here / "test_path.py"], ext="py")
    assert len(files) == 2


def test_collect_files__ignore_ext():
    files = path.collect_files([here / "test_config.py", here / "test_path.py"], ext="pyc")
    assert len(files) == 0
