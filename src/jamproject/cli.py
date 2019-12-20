import click
from click_default_group import DefaultGroup
from . import __version__


@click.group(cls=DefaultGroup, default="lint", default_if_no_args=True)
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    click.echo(f"{__name__.split('.')[0]} {__version__}")


@cmd.command()
def lint():
    """Lint files.
    """
    pass


def main():
    cmd()
