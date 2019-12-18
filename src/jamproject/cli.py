import click
from . import __version__


def display_version():
    """Display version.
    """
    package_name = __name__.split(".")[0]
    click.echo(f"{package_name} {__version__}")


@click.command()
@click.option("--version", is_flag=True)
def cmd(version):
    if version:
        display_version()
        return
    click.echo("Hello")


def main():
    cmd()
