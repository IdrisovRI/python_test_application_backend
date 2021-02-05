import json
import ast
import asyncio
from datetime import datetime
from typing import NoReturn
import aiohttp
from model.constant import MAIN_DATA_SOURCE
from model.point import Point
from helper.validate import PackageDataValidator
from dao.point_dao import PointDao
from helper.point import PointsHelper


# Нужно сделать: брать значения из базы а не прописывать на месте
IDS = {
    'EURUSD': 1,
    'USDJPY': 2,
    'GBPUSD': 3,
    'AUDUSD': 4,
    'USDCAD': 5
}


class LoaderService(object):
    """
    Сервис служит для загрузки данных из источника
    """
    running: bool

    def __init__(self):
        self.running = False

    async def __fetch(self, session, url):
        async with session.get(url) as response:
            return await response.text()

    async def __main(self):
        while self.running:
            async with aiohttp.ClientSession() as session:
                try:
                    # Осуществляем запрос и получаем результат
                    data_package = await self.__fetch(session, MAIN_DATA_SOURCE)
                    points = list()
                    if await PackageDataValidator.validate(data_package):
                        # Обрезаем ненужный мусор
                        data_package = data_package[5:-3]

                        # Производим преобразование пакета из строки в соответствующие типы
                        data = ast.literal_eval(data_package)

                        rates = data['Rates']
                        cur_time = datetime.now()

                        for rate in rates:
                            # Извлекаем тип валюты
                            symbol = rate['Symbol']

                            if symbol in IDS.keys():
                                point = Point(
                                    id=IDS[symbol],
                                    timestamp=int(cur_time.timestamp()),
                                    value=round((float(rate["Bid"])+float(rate["Ask"]))/2, 4)
                                )
                                # Добавляем значение в базу
                                await PointDao.insert(point)
                                points.append(point)
                                # print(point.__dict__)
                    PointsHelper().set(points)
                except Exception as ex:
                    print('LoaderService.__main Exception:{}'.format(ex))
                # Выжидаем секунду
                await asyncio.sleep(1)

    async def start(self) -> NoReturn:
        """
        Служит для запуска загрузки данных
        :return:
        """
        try:
            self.running = True
            await self.__main()
        except Exception as ex:
            self.running = False
            print('LoaderService.start Exception:{}'.format(ex))

    async def stop(self) -> NoReturn:
        """
        Служит для остановки загрузки данных
        :return:
        """
        if self.running:
            self.running = False
