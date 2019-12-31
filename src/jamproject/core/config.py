"""Configuration structure for jamproject
"""
from configparser import ConfigParser
from typing import Any, Dict
from pathlib import Path
from . import Config


base_key = "jamproject"


def _parse_config(path: Path) -> Config:
    """Parse configuration file.
    """
    config = {}
    cfg = ConfigParser()
    cfg.read(path)
    # TODO: Linting global params
    config = Config(cfg.items(base_key))
    config["skills"] = {}
    for section in cfg.sections():
        if not section.startswith(f"{base_key}."):
            continue
        skill_key = section[11:]
        # TODO: Linting skill params
        config["skills"][skill_key] = dict(cfg.items(section))
    return config


def load_config(path: Path, default=None) -> Config:
    if default is None:
        default_path = Path(__file__).parent / "default.cfg"
        config = _parse_config(default_path)
    else:
        config = default
    user_cfg = _parse_config(path)
    for k, v in user_cfg.items():
        if v:
            config[k] = v
    return config
