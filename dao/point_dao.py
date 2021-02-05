from typing import NoReturn
from model.point import Point
from dao.helper.db import AsyncDBHelper


class PointDao(object):
    @staticmethod
    async def insert(point: Point) -> NoReturn:
        """
        Метод служит для добавления записи в таблицу точек
        :param point: экземпляр класса точка
        :return:
        """
        # Определяется запрос на вставку данных
        query = """
            INSERT INTO "point"("id", "timestamp", "value")
            VALUES (:id, :timestamp, :value)
        """

        db_helper = AsyncDBHelper()

        await db_helper.connect()

        # Выполняем запрос
        await db_helper.execute(query, point.__dict__)

        # Фиксируется транзакция
        await db_helper.commit()

        # Закрываем соединение
        await db_helper.close()

    @staticmethod
    async def get_all(timestamp: int, asset_id: int):
        """
        Метод служит для вывода полного перечня доступных
        :return:
        """
        # Запрос на получение данных
        query = """
           SELECT "id", "timestamp", "value"
           FROM "point"
           WHERE "timestamp" > :timestamp and "id" = :id
        """

        db_helper = AsyncDBHelper()

        await db_helper.connect()

        # Параметры запроса
        params = {"id": asset_id, "timestamp": timestamp}

        # Выполняем запрос
        await db_helper.execute(query, params)

        # Извлекается результат выполнения
        result = await db_helper.fetch_all()

        # Закрываем соединение
        await db_helper.close()

        return result
