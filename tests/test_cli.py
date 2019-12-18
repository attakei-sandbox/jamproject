from jamproject.cli import version


def test_version(capsys):
    try:
        version()
    except SystemExit:
        pass
    captured = capsys.readouterr()
    assert captured.out == "jamproject 0.1.0\n"
