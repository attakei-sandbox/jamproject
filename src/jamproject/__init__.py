import click


__version__ = "0.1.0"


@click.group()
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    click.echo(f"{__name__} {__version__}")


def main():
    cmd()
