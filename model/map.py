from dataclasses import dataclass
from axis import Axis


@dataclass()
class Map:
    name: str
    description: str
    address: int
    factor: float

    x: Axis
    y: Axis
    z: Axis
