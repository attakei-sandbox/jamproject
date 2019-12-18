import click
from . import __version__


@click.group()
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    package_name = __name__.split(".")[0]
    click.echo(f"{package_name} {__version__}")


def main():
    cmd()
