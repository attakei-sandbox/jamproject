"""Core custom readers for docutils
"""
from typing import List, Type
from docutils import readers
from docutils.transforms import Transform
from .transforms import InitializeReportTransform, TokenizeTransform


class Reader(readers.Reader):
    """Basic custom reader class.

    Includes
    - Tokenize transform
    """

    def get_transforms(self) -> List[Type[Transform]]:
        """Return all transforms.
        """
        transforms = super().get_transforms()
        transforms += [TokenizeTransform, InitializeReportTransform]
        return transforms
