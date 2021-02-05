# Основной источник данных откуда происходит загрузка данных
MAIN_DATA_SOURCE = "https://ratesjson.fxcm.com/DataDisplayer"
# Определяется имя файла базы данных
DB_NAME = "point.db"

# Параметры для веб-сокета
# WS_HOST = "localhost"
WS_HOST = "127.0.0.1"
WS_PORT = 8080

# Переод времени за который берется выгрузка данных подписчику
MINUTE_PACKAGE_RANGE = 30
