from docutils.readers.standalone import Reader as BaseReader
from .transforms import Tokenize


class Reader(BaseReader):
    def __init__(self, parser=None, parser_name=None):
        super().__init__(parser=parser, parser_name=parser_name)
        self.skills = []

    def get_transforms(self):
        transforms = super().get_transforms()
        transforms.append(Tokenize)
        transforms += self.skills
        return transforms
