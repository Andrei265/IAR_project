import sqlite3


# Создание базы данных и таблицы с данными
def create_database():
    connection = sqlite3.connect("avb_db.db")  # Подключение к базе данных
    cursor = connection.cursor()

    # Создание таблицы "aircrafts"
    cursor.execute('''CREATE TABLE IF NOT EXISTS avb (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50),
                        length REAL,
                        class REAL,
                        x REAL,
                        y REAL
                    )''')

    # Заполнение таблицы данными
    aircrafts_data = [
        ("Милденхолл", 2800, 1, 52.365000000, 0.480833),
        ("Авиано", 3200, 1, 46.031388889, 12.596944444),
        ("Рамштайн", 2600, 2, 49.450000000, 7.550000000),
        ("Бандырма", 3500, 1, 40.319166667, 27.971388889),
        ("Шпангдалем", 3050, 1, 49.975833333, 6.697222222),
        ("Эрланн", 1700, 3, 63.699444444, 9.617222222),
        ("Ласк", 3000, 1, 51.583333333, 19.133333333),
        ("Тапа", 2400, 2, 59.238888889, 25.957222222),
        ("Эвенес", 3000, 1, 68.488888889, 16.678333333),
    ]

    cursor.executemany('''INSERT INTO avb (name, length, class, x, y)
                        VALUES (?, ?, ?, ?, ?)''', aircrafts_data)

    connection.commit()
    connection.close()


create_database() 