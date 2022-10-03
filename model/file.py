from dataclasses import dataclass
from map import Map


@dataclass
class File:
    filename: str
    softwarenumber: str
    partnumber: str
    boschPartnumber: str
    maps: list[Map]
