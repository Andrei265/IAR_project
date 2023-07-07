import sys
import sqlite3
import folium
import os
import math
import io
from branca.element import Figure


from PySide6.QtCore import QUrl
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QMessageBox
from PySide6.QtSql import QSqlTableModel
from PySide6.QtWebEngineWidgets import QWebEngineView

from main_ui import Ui_MainWindow
from map_ui import Ui_Dialog



class AircraftWindow(QMainWindow, QWebEngineView):
    def __init__(self):
        super(AircraftWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.populate_combo_box()
        self.ui.mmaapp.page().profile().clearHttpCache()

        # Привязка событий к кнопке
        self.ui.add_aircraft.clicked.connect(self.add_aircraft_to_table)
        self.ui.delete_aircraft.clicked.connect(self.delete_selected_aircraft)
        self.ui.avb.clicked.connect(self.avb_add)
        self.ui.map.clicked.connect(self.build_map)


    def populate_combo_box(self):
        # Подключение к базе данных
        connection = sqlite3.connect('aircrafts_db.db')
        cursor = connection.cursor()

        # Получение списка самолетов из базы данных
        cursor.execute('SELECT name FROM aircrafts')
        aircrafts = cursor.fetchall()

        # Заполнение выпадающего списка
        for aircraft in aircrafts:
            self.ui.comboBox.addItem(aircraft[0])

        # Закрытие соединения с базой данных
        cursor.close()
        connection.close()

    def add_aircraft_to_table(self):
        # Получение выбранного самолета из выпадающего списка
        selected_aircraft = self.ui.comboBox.currentText()

        # Подключение к базе данных
        connection = sqlite3.connect('aircrafts_db.db')
        cursor = connection.cursor()

        # Получение информации о выбранном самолете из базы данных
        cursor.execute('SELECT * FROM aircrafts WHERE name=?', (selected_aircraft,))
        aircraft = cursor.fetchone()

        # Добавление информации в таблицу
        row_count = self.ui.aircraft_table.rowCount()
        self.ui.aircraft_table.insertRow(row_count)
        for column_number, data in enumerate(aircraft):
            if column_number != 0:
                self.ui.aircraft_table.setItem(row_count, column_number-1, QTableWidgetItem(str(data)))

        # Закрытие соединения с базой данных
        cursor.close()
        connection.close()

    def delete_selected_aircraft(self):
        # Получение текущей выбранной строки
        selected_row = self.ui.aircraft_table.currentRow()
        
        if selected_row >= 0:
            # Удаление выбранной строки
            self.ui.aircraft_table.removeRow(selected_row)
        else:
            QMessageBox.warning(self, 'Ошибка', 'Нет выбранной строки для удаления.')

    def avb_add(self):
        row_count = self.ui.avb_table.rowCount()

        for row in range(row_count):
            self.ui.avb_table.removeRow(0)
        # Подключение к базе данных
        connection = sqlite3.connect('avb_db.db')
        cursor = connection.cursor()

        row_count = self.ui.aircraft_table.rowCount()
        column_count = self.ui.aircraft_table.columnCount()


        data = []
        m = []
        d = []
        for row in range(row_count):
            row_data = []
            for column in range(column_count):
                item = self.ui.aircraft_table.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)
            m.append(float(row_data[1]))
            d.append(float(row_data[3]))
        
        l = max(m)
        mass = max(d)
        print(l)
        print(mass)
        if mass >= 75000:
            f = 1
        elif mass >= 30000 and mass < 75000:
            f = 2
        elif mass >= 10000 and mass < 30000:
            f = 3
        else:
            f = 4
        # Получение информации о выбранном самолете из базы данных
        cursor.execute('SELECT * FROM avb WHERE class<=? AND length>=?', (f, l*0.9,))
        avbs = cursor.fetchall()
        print(avbs)
        # Добавление информации в таблицу
        for i in avbs:
            row_count = self.ui.avb_table.rowCount()
            self.ui.avb_table.insertRow(row_count)
            if avbs != None:
                for column_number, data in enumerate(i):
                    if column_number != 0:
                        self.ui.avb_table.setItem(row_count, column_number-1, QTableWidgetItem(str(data)))
            else:
                print('GG')
        # Закрытие соединения с базой данных
        cursor.close()
        connection.close()
        
    def build_map(self):
        row_count = self.ui.aircraft_table.rowCount()
        column_count = self.ui.aircraft_table.columnCount()

        data = []
        d2e = []
        d2f = []
        for row in range(row_count):
            row_data = []
            for column in range(column_count):
                item = self.ui.aircraft_table.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)
            d2e.append(float(row_data[5]))
            d2f.append(float(row_data[7]))
        
        r_empty = min(d2e)
        r_full = min(d2f)
        row_count = self.ui.avb_table.rowCount()
        column_count = self.ui.avb_table.columnCount()

        data = []
        x = []
        y = []
        nms = []
        for row in range(row_count):
            row_data = []
            for column in range(column_count):
                item = self.ui.avb_table.item(row, column)
                if item is not None:
                    row_data.append(item.text())
                else:
                    row_data.append("")
            data.append(row_data)
            x.append(float(row_data[3]))
            y.append(float(row_data[4]))
            nms.append(str(row_data[0]))

        m = folium.Map(tiles='OpenStreetMap', location=[55.751244, 37.618423], zoom_start=4, control_scale=True)
        print("+++++++++++++++++++++++++++++++++++++")
        print(nms)
        print(x)
        print(y)
        r1 = r_empty
        r2 = r_full
        fig = Figure()
        mp = folium.plugins.MousePosition().add_to(fig)

        for n, x, y in zip(nms, x, y):
            marker = folium.Marker([x, y], popup=str(n))
            marker.add_to(m)
            folium.CircleMarker([x, y], radius=r1/75, color='yellow', fill=True, fill_color='yellow', fill_opacity=0.1, no_touch=False).add_to(marker)
            folium.CircleMarker([x, y], radius=r2/75, color='green', fill=True, fill_color='green', fill_opacity=0.1, no_touch=False).add_to(marker)
            marker.add_to(fig)
        m.add_child(fig)
        # Сохранение карты в HTML-файл
        data = io.BytesIO()
        m.save(data, close_file=False)


        # Загрузка HTML-файла с картой в QWebEngineView
        self.ui.mmaapp.load(QUrl.fromLocalFile(os.path.abspath('map.html')))
        self.ui.mmaapp.setHtml(data.getvalue().decode())
        self.ui.mmaapp.show()

if __name__ == '__main__':
    # Создание приложения PyQt
    app = QApplication(sys.argv)

    # Создание и отображение окна
    window = AircraftWindow()
    window.show()

    # Запуск основного цикла приложения
    sys.exit(app.exec())
