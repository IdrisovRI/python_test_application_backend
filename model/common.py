class CommandData(object):
    """
    Класс в котором хранятся входящий пакет информации
    """
    action: str
    message: dict

    def __init__(self, ws, action: str, message: dict):
        self.ws = ws
        self.action = action
        self.message = message
