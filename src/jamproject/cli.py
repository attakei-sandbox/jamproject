import click
from click_default_group import DefaultGroup
from docutils.core import publish_file
from . import __version__
from .core.readers import Reader
from .core.writers import Writer
from .skills import reporting


@click.group(cls=DefaultGroup, default="run", default_if_no_args=True)
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    click.echo(f"{__name__.split('.')[0]} {__version__}")


@cmd.command()
@click.argument('target', type=click.Path(exists=True), )
def run(target):
    """Lint files.
    """
    reader = Reader()
    reader.add_skill(reporting.Skill())
    publish_file(source_path=target, reader=reader, writer=Writer())


def main():
    cmd()
