import json
from model.common import CommandData
from dao.asset_dao import AssetDao


class AssetsCmd(object):
    """
    Команда служит для получения перечня активов
    """
    async def execute(self, cd: CommandData):
        # Получаем данные из базы данных
        data = await AssetDao.get_all()

        # Подготавливаем сообщение к отправке
        message = json.dumps({"action": "assets", "message": data})

        await cd.ws.send(str(message))
