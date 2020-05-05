"""Path management.
"""
from pathlib import Path
from typing import List


def collect_files(files: List[Path], ext: str=None) -> List[Path]:
    """Collect files having ext.

    :params files: Candidate of files
    :params ext: Filtering extension
    :returns: Globbed **file** list (exclude directory)
    """
    glob = f"**/*" if ext is None else f"**/*.{ext}"
    rslt = []
    for f in files:
        if f.is_dir():
            rslt += [f for f in f.glob(glob) if f.is_file()]
            continue
        if ext is None:
            rslt.append(f)
            continue
        if f.suffix[1:] == ext:
            rslt.append(f)
            continue
    return rslt
