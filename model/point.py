from dataclasses import dataclass


@dataclass
class Point(object):
    """
    Класс с данными точки
    """
    id: int
    timestamp: int
    value: float
