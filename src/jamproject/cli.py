import click
from pprint import pprint
from pathlib import Path
from typing import List, Optional
from . import __version__


def display_version():
    """Display version.
    """
    package_name = __name__.split(".")[0]
    click.echo(f"{package_name} {__version__}")


def collect_all_sources(
    targets: List[str], extensions: List[str], basepath: Optional[Path] = None
) -> List[Path]:
    """Collect file sources.

    :param targes: Collect target resources(include files and directories)
    :param extensions: List of target extension (used fo directory)
    :return: Matched files
    """
    basepath = Path.cwd() if basepath is None else basepath
    sources: List[Path] = []
    for t in targets:
        target = basepath / t
        if target.is_file():
            sources += [
                target,
            ]
            continue
        sources += [p for p in target.glob("**/*") if p.suffix in extensions]
    return sources


@click.command()
@click.option("--version", is_flag=True)
@click.option(
    "--verbose", "-v", is_flag=True,
)
@click.argument("targets", nargs=-1, type=click.Path(exists=True))
def cmd(version, verbose, targets):
    if version:
        display_version()
        return
    target_files = collect_all_sources(targets, [".rst"], Path.cwd())
    pprint(target_files)


def main():
    cmd()
