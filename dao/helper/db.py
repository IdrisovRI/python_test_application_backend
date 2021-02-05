import aiosqlite
import asyncio
from model.constant import DB_NAME


class AsyncDBHelper(object):
    """
    Класс служит для работы с БД
    """
    __conn = None
    __cursor = None

    async def connect(self):
        self.__conn = await aiosqlite.connect(DB_NAME, loop=asyncio.get_event_loop())
        self.__conn.row_factory = aiosqlite.Row
        self.__cursor = await self.__conn.cursor()

    async def execute(self, script: str, params: dict):
        """
        Производится выполнение скрипта
        :param script: Скрипт для выполнения
        :param params: Параметры запроса
        :return:
        """
        await self.__cursor.execute(script, params)
        return self

    async def commit(self):
        await self.__conn.commit()

    async def fetch_one(self):
        """
        Производит извлечение одной записи из результатов запроса
        :return:
        """
        row = await self.__cursor.fetchone()

        row = dict(row)

        return row

    async def fetch_all(self):
        """
        Производит извлечение всех записей из результатов запроса
        :return:
        """

        # rows = await self.__cursor.fetchall()

        result = []
        for row in await self.__cursor.fetchall():
            result.append(dict(row))

        return result
        # rows = await self.__cursor.fetchall()
        # print('ROWS:{}'.format(rows))
        # print('ROWS:{}'.format(dict(rows)))
        #
        #
        # return rows

    async def close(self):
        """
        Закрытие всех соединений
        :return:
        """
        await self.__cursor.close()
        await self.__conn.close()
