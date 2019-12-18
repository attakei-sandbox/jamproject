import pytest
from pathlib import Path
from jamproject.cli import collect_all_sources, display_version


here = Path(__file__).parent.resolve()


def test_version(capsys):
    display_version()
    captured = capsys.readouterr()
    assert captured.out == "jamproject 0.1.0\n"


@pytest.mark.parametrize(
    "targets,ext,files",
    [
        (["./testdata/collect_all_sources"], [".rst"], 1),
        (["./testdata/collect_all_sources"], [".rst", ".txt"], 2),
        (["./testdata/collect_all_sources/index.rst"], [], 1),
    ],
)
def test_collect_all_sources(targets, ext, files):
    sources = collect_all_sources(targets, ext, here)
    assert len(sources) == files
