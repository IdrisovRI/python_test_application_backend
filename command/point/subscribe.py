import json
from datetime import datetime, timedelta
from model.common import CommandData
from helper.subscriber import UserSubscribeHelper
from dao.point_dao import PointDao
from model.constant import MINUTE_PACKAGE_RANGE


class SubscribeCmd(object):
    """
    Команда служит для подписки
    """
    async def execute(self, cd: CommandData):
        message = cd.message
        # Извлекается идентификатор валюты
        asset_id = message['assetId']
        # Подписываем пользователя на отправку
        UserSubscribeHelper().subscribe(cd.ws, asset_id)
        # Задается стартовое время
        timestamp = int((datetime.now() - timedelta(minutes=MINUTE_PACKAGE_RANGE)).timestamp())
        # Получаем их базы пакет данных
        package_data = await PointDao.get_all(timestamp, asset_id)
        # Формируется сообщение для отправки
        message = json.dumps({"message": {"points": package_data}, "action": "asset_history"})

        await cd.ws.send(message)
