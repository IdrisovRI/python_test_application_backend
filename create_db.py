import sqlite3
from model.constant import DB_NAME

# Определение соединения с бд
conn = sqlite3.connect(DB_NAME)
cursor = conn.cursor()

# Создание таблиц
cursor.execute("""CREATE TABLE "point" ("id" INTEGER NOT NULL, "timestamp" INTEGER NOT NULL, "value" REAL NOT NULL)""")
cursor.execute("""CREATE TABLE "asset" ("id" INTEGER PRIMARY KEY NOT NULL, "symbol" TEXT NOT NULL)""")

# Создание индексов
cursor.execute("""CREATE INDEX IF NOT EXISTS "i_point_id" ON "point"("id")""")
cursor.execute("""CREATE INDEX IF NOT EXISTS "i_point_timestamp" ON "point"("timestamp")""")

# Создание записей
cursor.execute("""INSERT INTO "asset"("id", "symbol") VALUES (1, 'EURUSD')""")
cursor.execute("""INSERT INTO "asset"("id", "symbol") VALUES (2, 'USDJPY')""")
cursor.execute("""INSERT INTO "asset"("id", "symbol") VALUES (3, 'GBPUSD')""")
cursor.execute("""INSERT INTO "asset"("id", "symbol") VALUES (4, 'AUDUSD')""")
cursor.execute("""INSERT INTO "asset"("id", "symbol") VALUES (5, 'USDCAD')""")

# Фиксирование изменений
conn.commit()

# Закрытие всех соединений
cursor.close()
conn.close()
