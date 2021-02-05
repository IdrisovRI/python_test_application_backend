from dataclasses import dataclass


@dataclass
class Asset(object):
    """
    Класс с данными актива
    """
    id: int
    symbol: str
