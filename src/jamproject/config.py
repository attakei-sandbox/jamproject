"""Configuration for jamproject
"""
import configparser
from pathlib import Path
from typing import List, Optional


def find_filepath(basedir: Path, targets: List[str]) -> Optional[Path]:
    """Find target from candidates

    :param basedir: Find target directrory
    :param targets: Candidates of target file
    :return: Exists file path or None
    """
    for t in targets:
        target = basedir / t
        if target.exists() and target.is_file():
            return target
    return None
