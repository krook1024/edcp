from dataclasses import dataclass


@dataclass
class Axis:
    address: str
    description: str
    factor: float
    unit: str
