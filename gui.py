import sys
import sqlite3
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QListWidget, QGraphicsScene, QLabel
from PyQt6.QtGui import QPixmap, QPen, QColor, QBrush, QPainterPath
from PyQt5.QtCore import Qt, QPointF
import folium


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Aircraft Application")
        self.setGeometry(100, 100, 800, 600)

        self.init_ui()
        self.add_review_button.clicked.connect(self.add_aircraft_to_review)
        self.add_list_button.clicked.connect(self.add_aircraft_to_list)
        self.build_map_button.clicked.connect(self.build_map)
        self.calculate_airbases_button.clicked.connect(self.calculate_airbases)

        self.selected_aircraft = None
        self.reviewed_aircraft = []

    def init_ui(self):
        # Создание главного виджета и размещение его в окне
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Создание вертикального лейаута для размещения элементов интерфейса
        layout = QVBoxLayout(main_widget)

        # Создание списка самолетов
        self.aircraft_list = QListWidget()
        layout.addWidget(self.aircraft_list)

        # Создание кнопок "Добавить самолет к рассмотрению" и "Добавить самолет в список"
        button_layout = QHBoxLayout()
        self.add_review_button = QPushButton("Добавить самолет к рассмотрению")
        self.add_list_button = QPushButton("Добавить самолет в список")
        button_layout.addWidget(self.add_review_button)
        button_layout.addWidget(self.add_list_button)
        layout.addLayout(button_layout)

        # Создание виджета для отображения фото самолета
        self.aircraft_image = QLabel()
        layout.addWidget(self.aircraft_image)

        # Создание списка авиабаз
        self.airbase_list = QListWidget()
        layout.addWidget(self.airbase_list)

        # Создание кнопок "Построить карту" и "Расчет Авб"
        self.build_map_button = QPushButton("Построить карту")
        self.calculate_airbases_button = QPushButton("Расчет Авб")
        layout.addWidget(self.build_map_button)
        layout.addWidget(self.calculate_airbases_button)

    def update_aircraft_list(self):
        aircraft = get_aircraft()
        self.aircraft_list.clear()

        for item in aircraft:
            name = item[0]
            self.aircraft_list.addItem(name)

    def update_airbase_list(self, airbases):
        self.airbase_list.clear()

        for airbase in airbases:
            name = airbase[0]
            self.airbase_list.addItem(name)

    def add_aircraft_to_review(self):
        if self.aircraft_list.currentItem() is not None:
            selected_aircraft = self.aircraft_list.currentItem().text()
            self.reviewed_aircraft.append(selected_aircraft)
            self.update_reviewed_aircraft()

    def add_aircraft_to_list(self):
        if self.aircraft_list.currentItem() is not None:
            selected_aircraft = self.aircraft_list.currentItem().text()
            self.selected_aircraft = selected_aircraft
            self.update_selected_aircraft()

    def update_reviewed_aircraft(self):
        self.reviewed_aircraft_list.clear()

        for item in self.reviewed_aircraft:
            self.reviewed_aircraft_list.addItem(item)

    def update_selected_aircraft(self):
        if self.selected_aircraft:
            conn = sqlite3.connect('aircraft.db')
            c = conn.cursor()

            # Получение информации о выбранном самолете
            c.execute("SELECT * FROM aircraft WHERE name=?", (self.selected_aircraft,))
            aircraft_info = c.fetchone()

            conn.close()

            if aircraft_info:
                name, image_path, description = aircraft_info

                # Отображение фото самолета в виджете
                pixmap = QPixmap(image_path)
                self.aircraft_image.setPixmap(pixmap.scaled(300, 200))

                # Отображение информации о самолете в соответствующих виджетах
                self.aircraft_name_label.setText(name)
                self.aircraft_description_label.setText(description)

    def get_min_practical_range(selected_aircraft):
        # Получение минимальной практической дальности выбранных самолетов
        min_practical_range = float('inf')  # Инициализируем значением бесконечности

        for aircraft in selected_aircraft:
            practical_range = aircraft['practical_range']
            if practical_range < min_practical_range:
                min_practical_range = practical_range

        return min_practical_range


    def get_min_ferry_range(selected_aircraft):
        # Получение минимальной перегоночной дальности выбранных самолетов
        min_ferry_range = float('inf')  # Инициализируем значением бесконечности

        for aircraft in selected_aircraft:
            ferry_range = aircraft['ferry_range']
            if ferry_range < min_ferry_range:
                min_ferry_range = ferry_range

        return min_ferry_range


    def build_map(self):
        # Создание графической сцены для карты
        scene = QGraphicsScene(self)
        self.map_graphics_view.setScene(scene)

        # Получение выбранных самолетов для рассмотрения
        selected_aircraft = self.reviewed_aircraft

        # Получение списка авиабаз из базы данных airbase.db
        conn = sqlite3.connect('airbase.db')
        c = conn.cursor()
        c.execute("SELECT * FROM airbase")
        airbases = c.fetchall()
        conn.close()

        # Отображение авиабаз на карте
        for airbase in airbases:
            name, location, runway_length = airbase

            # Отображение метки авиабазы
            x, y = location.split(',')
            x = float(x.strip())
            y = float(y.strip())
            scene.addEllipse(x - 5, y - 5, 10, 10, QPen(Qt.black), QBrush(Qt.black))
            scene.addText(name).setPos(x + 10, y)

            # Получение минимальной практической дальности и перегоночной дальности
            # выбранных самолетов для рассмотрения
            practical_range = self.get_min_practical_range(selected_aircraft)
            ferry_range = self.get_min_ferry_range(selected_aircraft)

            # Отображение зеленого круга с радиусом практической дальности
            green_radius = practical_range * 1000  # Перевод дальности в метры
            green_circle = scene.addEllipse(x - green_radius, y - green_radius,
                                            2 * green_radius, 2 * green_radius,
                                            QPen(Qt.green), QBrush(QColor(0, 255, 0, 40)))
            green_circle.setZValue(-1)  # Помещаем круг ниже авиабазы и других элементов на сцене

            # Отображение желтого круга с радиусом перегоночной дальности
            yellow_radius = ferry_range * 1000  # Перевод дальности в метры
            yellow_circle = scene.addEllipse(x - yellow_radius, y - yellow_radius,
                                            2 * yellow_radius, 2 * yellow_radius,
                                            QPen(Qt.yellow), QBrush(QColor(255, 255, 0, 40)))
            yellow_circle.setZValue(-1)  # Помещаем круг ниже авиабазы и других элементов на сцене

    def get_min_takeoff_length(selected_aircraft):
        # Получение минимальной длины разбега выбранных самолетов
        min_takeoff_length = float('inf')  # Инициализируем значением бесконечности

        for aircraft in selected_aircraft:
            takeoff_length = aircraft['takeoff_length']
            if takeoff_length < min_takeoff_length:
                min_takeoff_length = takeoff_length

        return min_takeoff_length


    def get_min_landing_length(selected_aircraft):
        # Получение минимальной длины пробега выбранных самолетов
        min_landing_length = float('inf')  # Инициализируем значением бесконечности

        for aircraft in selected_aircraft:
            landing_length = aircraft['landing_length']
            if landing_length < min_landing_length:
                min_landing_length = landing_length

        return min_landing_length


    def get_min_takeoff_weight(selected_aircraft):
        # Получение минимальной взлетной массы выбранных самолетов
        min_takeoff_weight = float('inf')  # Инициализируем значением бесконечности

        for aircraft in selected_aircraft:
            takeoff_weight = aircraft['takeoff_weight']
            if takeoff_weight < min_takeoff_weight:
                min_takeoff_weight = takeoff_weight

        return min_takeoff_weight


    def calculate_airbases(self, selected_aircraft, airbase_list):
        valid_airbases = []

        min_takeoff_length = self.get_min_takeoff_length(selected_aircraft)
        min_landing_length = self.get_min_landing_length(selected_aircraft)
        min_takeoff_weight = self.get_min_takeoff_weight(selected_aircraft)

        for airbase in airbase_list:
            runway_length = airbase['runway_length']

            if runway_length >= 3000:
                valid_airbases.append(airbase)
            elif 2000 <= runway_length < 3000 and min_takeoff_weight <= 75000:
                valid_airbases.append(airbase)
            elif runway_length < 2000 and min_takeoff_weight <= 30000:
                valid_airbases.append(airbase)

        return valid_airbases


def get_aircraft():
    conn = sqlite3.connect('aircraft.db')
    c = conn.cursor()

    c.execute("SELECT * FROM aircraft")
    aircraft = c.fetchall()

    conn.close()

    return aircraft

def get_airbases():
    conn = sqlite3.connect('airbase.db')
    c = conn.cursor()

    c.execute("SELECT * FROM airbase")
    airbases = c.fetchall()

    conn.close()

    return airbases

def create_map(airbases):
    map = folium.Map()

    for airbase in airbases:
        name = airbase[0]
        location = airbase[1]
        lat, lon = location.split(',')

        folium.Marker([lat, lon], popup=name).add_to(map)

    return map


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
