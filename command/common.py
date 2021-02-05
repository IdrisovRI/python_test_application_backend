from command.asset.assets import AssetsCmd
from command.point.subscribe import SubscribeCmd


class CommandFactory(object):
    commands = dict()

    def __init__(self):
        self.commands = dict()
        self.__build_commands()

    def get_command(self, key: str):
        """
        Функция возвращает command по ключу
        :param  key: - Название команды
        :return
        """
        if key in self.commands:
            return self.commands[key]
        return None

    def __build_commands(self):
        """
        Функция определяет перечень доступных комманд
        """
        self.commands = {
            'assets': AssetsCmd(),
            'subscribe': SubscribeCmd()
        }