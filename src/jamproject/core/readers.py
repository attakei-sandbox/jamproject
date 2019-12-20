"""Core custom readers for docutils
"""
from typing import List, Type
from docutils import readers, transforms
from .transforms import Tokenize


class Reader(readers.Reader):
    """Basic custom reader class.

    Includes
    - Tokenize transform
    """

    def get_transforms(self) -> List[Type[transforms.Transform]]:
        """Return all transforms.
        """
        return super().get_transforms() + [Tokenize]
