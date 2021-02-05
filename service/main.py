import asyncio
from service.loader import LoaderService
from service.web_socket import WSService
from model.constant import WS_HOST, WS_PORT


class MainService(object):
    """
    Основной сервис
    """
    def __init__(self, name: str):
        self.name = name
        self.loop = asyncio.get_event_loop()
        self.loader_service = LoaderService()
        self.ws_service = WSService(WS_HOST, WS_PORT)

    def start(self):
        self.loop.create_task(self.loader_service.start())
        self.loop.run_until_complete(self.ws_service.server)
        self.loop.run_forever()

    def stop(self):
        self.loader_service.stop()
