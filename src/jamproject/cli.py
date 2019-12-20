import click
from . import __version__


@click.group()
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    click.echo(f"{__name__.split('.')[0]} {__version__}")


def main():
    cmd()
