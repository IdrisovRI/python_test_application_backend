from dao.helper.db import AsyncDBHelper


class AssetDao(object):
    @staticmethod
    async def get_all():
        """
        Метод служит для вывода полного перечня доступных
        :return:
        """
        # Запрос на получение данных
        query = """
           SELECT "id", "symbol"
           FROM "asset"
        """

        db_helper = AsyncDBHelper()

        await db_helper.connect()

        # Поскольку запрос без параметров, то используем пустой
        params = {}

        # Выполняем запрос
        await db_helper.execute(query, params)

        # Извлекается результат выполнения
        result = await db_helper.fetch_all()

        # Закрываем соединение
        await db_helper.close()

        return result
