import tempfile
import click
from pathlib import Path
from click_default_group import DefaultGroup
from docutils.core import publish_file
from . import __version__
from .config import load_config, load_default_config
from .skill import load_skills
from .readers import Reader
from .utils.path import collect_files, resolve_path
from .writers import Writer


@click.group(cls=DefaultGroup, default="docutils", default_if_no_args=True)
def cmd():
    pass


@cmd.command()
def version():
    """Display version.
    """
    click.echo(f"{__name__.split('.')[0]} {__version__}")


@cmd.command()
@click.argument(
    "targets", type=click.Path(exists=True), nargs=-1,
)
def docutils(targets):
    """Lint files.
    """
    targets = tuple(resolve_path(t) for t in targets)
    config_path: Path = Path.cwd() / "setup.cfg"
    if config_path.exists():
        config = load_config(config_path)
    else:
        config = load_default_config()
    reader = Reader()
    for skill in load_skills(config):
        reader.add_skill(skill)
    # Collect files
    collected = collect_files(targets, "rst")
    # Lint all files
    for target in collected:
        publish_file(source_path=target, reader=reader, writer=Writer())


@cmd.command()
@click.argument(
    "conf", type=click.Path(exists=True),
)
@click.argument(
    "targets", type=click.Path(exists=True), nargs=-1,
)
def sphinx(conf, targets):
    try:
        from sphinx.application import Sphinx
    except ImportError:
        click.echo("sphinx command is require 'sphinx' package.")
        return
    if not targets:
        targets = (Path(conf).parent,)
    targets = tuple(resolve_path(t) for t in targets)
    config_path: Path = Path.cwd() / "setup.cfg"
    if config_path.exists():
        config = load_config(config_path)
    else:
        config = load_default_config()
    wk_dir = Path(tempfile.mkdtemp())
    conf_dir = Path(conf).resolve().parent
    app = Sphinx(conf_dir, conf_dir, wk_dir / "out", wk_dir / "doctree", "dummy")
    app.builder.read()
    print("")
    reader = Reader()
    for skill in load_skills(config):
        reader.add_skill(skill)
    # Collect files
    collected = collect_files(targets, "rst")
    # Lint all files
    for target in collected:
        t = target.relative_to(conf_dir)
        t = f"{str(t.parent)}/{t.stem}"
        if t.startswith("./"):
            t = t[2:]
        app.env.prepare_settings(str(t))
        publish_file(
            source_path=target,
            reader=reader,
            writer=Writer(),
            settings_overrides=app.env.settings,
        )


def main():
    cmd()
