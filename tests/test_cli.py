from jamproject.cli import display_version


def test_version(capsys):
    display_version()
    captured = capsys.readouterr()
    assert captured.out == "jamproject 0.1.0\n"
