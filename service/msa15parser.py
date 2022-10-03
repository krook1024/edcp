from model.file import File
from parser import Parser

"""
https://github.com/Blackfrosch/VAGEDCSuite/blob/master/MSA15FileParser.cs
"""


class Msa15Parse(Parser):
    def should_parse(self, file: File) -> bool:
        return True

    def parse_maps(self, file: File) -> File:
        pass
