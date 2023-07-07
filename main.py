import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtGui import QPixmap


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('My App')
        self.setGeometry(100, 100, 800, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Виджет с картой мира Folium
        self.map_view = QWebEngineView()
        self.map_view.load(QtCore.QUrl.fromLocalFile('<путь к файлу HTML с картой>'))
        self.layout.addWidget(self.map_view)

        # Виджет для отображения фотографии
        self.photo_label = QLabel()
        self.layout.addWidget(self.photo_label)

        # Виджет для отображения текста
        self.text_label = QLabel()
        self.layout.addWidget(self.text_label)

        # Загрузка фотографии
        self.load_photo('<путь к фотографии>')

        # Отображение текста
        self.display_text('Пример текста')

    def load_photo(self, path):
        pixmap = QPixmap(path)
        self.photo_label.setPixmap(pixmap.scaledToWidth(400))

    def display_text(self, text):
        self.text_label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())
