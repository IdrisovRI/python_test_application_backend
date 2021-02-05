from typing import NoReturn, List
from model.point import Point


class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class PointsHelper(object, metaclass=Singleton):
    """
    Служит для хранения последних полученных курсов
    """
    points = []

    def set(self, points: List[Point]) -> NoReturn:
        """
        Служит для установки последнего полученного пакета
        :param points: Перечень точек
        :return:
        """
        self.points = points

    def get_point_by_id(self, asset_id: int):
        """
        Метод служит для получения точки по ее идентификатору
        :param asset_id: Идентификатор точки
        :return:
        """
        result = None
        if self.points:
            for point in self.points:
                if point.id == asset_id:
                    result = point
        return result
