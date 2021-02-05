from typing import Optional, NoReturn


class UserSubscribeHelper(object):
    """
    Помошник для работы с
    """
    users = {}

    def subscribe(self, ws, asset_id: int) -> NoReturn:
        """
        Добавить подписчика
        """
        self.users[ws] = asset_id

    def unsubscribe(self, ws) -> NoReturn:
        """
        Убрать пользователя из перечня подписантов
        """
        self.users.pop(ws, None)

    def get_asset_id(self, ws) -> Optional[int]:
        """
        Служит для получения идентификатора подписки
        """
        asset_id = None
        if ws in self.users:
            asset_id = self.users[ws]
        return asset_id
