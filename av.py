import sqlite3

# Создание базы данных и таблицы с данными
def create_database():
    connection = sqlite3.connect("aircrafts_db.db")  # Подключение к базе данных
    cursor = connection.cursor()

    # Создание таблицы "aircrafts"
    cursor.execute('''CREATE TABLE IF NOT EXISTS aircrafts (
                        ID INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(50),
                        distance_takeoff REAL,
                        distance_landing REAL,
                        max_mass REAL,
                        oneway_empty_range REAL,
                        oneway_equip_range REAL,
                        roundtrip_empty_range REAL,
                        roundtrip_equip_range REAL
                    )''')

    # Заполнение таблицы данными
    aircrafts_data = [
        ("Rockwell B-1A Lancer", 3048, 2152, 176800, 10500, 9817, 5150, 4808.5),
        ("Rockwell B-1B Lancer", 3700, 2740, 216363, 11998, 9254, 5899, 4527),
        ("Northrop B-2 Spirit", 3048, 2134, 170600, 11100, 9600, 5450, 4700),
        ("Boeing B-52 Stratofortress", 3048, 2195, 220000, 16000, 12000, 7900, 5900),
        ("McDonnell Douglas F-15E", 2475, 1830, 36700, 4800, 3400, 2300, 1600),
        ("Lockheed/Boeing F-22 Raptor", 1524, 914, 38000, 3200, 2960, 1500, 1380),
        ("General Dynamics F-16", 1830, 1220, 19187, 4220, 2575, 2010, 1187.5),
        ("Fairchild Republic A-10", 1067, 732, 22950, 1800, 1600, 800, 700),
        ("Lockheed AC-130 Spectre", 1091, 518, 79380, 3200, 2400, 1600, 1100),
        ("Boeing C-17 Globemaster III", 2360, 915, 265350, 8710, 4445, 4355, 2122.5),
        ("Alenia C-27J Spartan", 1050, 700, 305000, 5556, 2778, 2778, 1289),
        ("C-41A Aviocar", 775, 425, 75000, 1334, 8500, 667, 4150),
        ("C-130E/H Hercules", 975, 735, 70300, 5930, 3620, 2965, 1710),
        ("C-130J Super Hercules", 1524, 914, 79378, 7790, 5200, 3895, 2500),
        ("Boeing KC-135 Stratotanker", 2743, 1524, 146295, 4570, 4200, 2285, 2000),
        ("McDonnell Douglas KC-10 Extender", 3658, 2134, 267620, 9420, 7800, 4710, 3800),
        ("Lockheed Martin KC-130", 945, 762, 70305, 3330, 3090, 1665, 1445)

    ]

    cursor.executemany('''INSERT INTO aircrafts (name, distance_takeoff, distance_landing, max_mass, 
                        oneway_empty_range, oneway_equip_range, roundtrip_empty_range, roundtrip_equip_range)
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?)''', aircrafts_data)

    connection.commit()
    connection.close()


create_database()
