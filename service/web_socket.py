import asyncio
import websockets
import ast
import json
from command.common import CommandFactory
from model.common import CommandData
from helper.subscriber import UserSubscribeHelper
from helper.point import PointsHelper

# Необходимо добавить логику с выгрузкой из базы
ASSET_NAMES = {
    1: 'EURUSD',
    2: 'USDJPY',
    3: 'GBPUSD',
    4: 'AUDUSD',
    5: 'USDCAD'
}


class WSService(object):

    def __init__(self, host: str, port: int):
        self.server = websockets.serve(
            ws_handler=self.main,
            host=host,
            port=port
        )

    async def consumer_handler(self, ws, path):
        async for message in ws:
            if 'action' in message and "message" in message:
                message = ast.literal_eval(message)
                action = message['action']

                # Получаем команду
                command = CommandFactory().get_command(action)
                if command:
                    cd = CommandData(
                        ws=ws,
                        action=message['action'],
                        message=message['message']
                    )
                    # Производится запуск соответствующей команды
                    await command.execute(cd)

    async def producer_handler(self, ws, path):
        while True:
            asset_id = UserSubscribeHelper().get_asset_id(ws=ws)
            if asset_id:
                point = PointsHelper().get_point_by_id(asset_id)
                if point:
                    message = json.dumps({
                        "message": {
                            "assetName": ASSET_NAMES[point.id],
                            "time": point.timestamp,
                            "assetId": point.id,
                            "value": point.value
                        }, "action": "point"}
                    )

                    await ws.send(message)
            await asyncio.sleep(1)

    async def main(self, ws, path):
        consumer_task = asyncio.ensure_future(self.consumer_handler(ws, path))
        producer_task = asyncio.ensure_future(self.producer_handler(ws, path))
        done, pending = await asyncio.wait(
            [consumer_task, producer_task],
            return_when=asyncio.FIRST_COMPLETED,
        )
        for task in pending:
            task.cancel()
