import pytest
from pathlib import Path
from motto.core import path

here = Path(__file__).parent.resolve()


@pytest.mark.parametrize("ext,expect", [(None, 2), ("txt", 1)])
def test_collect_files__case_ext(ext, expect):
    files = path.collect_files([here / "test_path_data"], ext=ext)
    assert len(files) == expect


def test_collect_files__multilpe_files():
    files = path.collect_files(
        [here / "test_config.py", here / "test_path.py"], ext="py"
    )
    assert len(files) == 2


def test_collect_files__ignore_ext():
    files = path.collect_files(
        [here / "test_config.py", here / "test_path.py"], ext="pyc"
    )
    assert len(files) == 0


@pytest.mark.parametrize("src", [(None,), ([],)])
def test_resolve_path__raises(src):
    with pytest.raises(TypeError):
        path.resolve_path(src)


@pytest.mark.parametrize("src", ["./test_config", ".",])
def test_resolve_path__strings(src):
    resolved = path.resolve_path(src)
    assert isinstance(resolved, Path)


def test_resolve_path__path_resolved():
    src = Path(".")
    resolved = path.resolve_path(src)
    assert str(src) != str(resolved)
