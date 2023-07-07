from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton


class SecondWindow(QMainWindow):
    def __init__(self):
        super(SecondWindow, self).__init__()

        # Создание кнопки "Закрыть"
        self.close_button = QPushButton('Закрыть')
        self.close_button.clicked.connect(self.close)

        # Установка кнопки "Закрыть" во второе окно
        self.setCentralWidget(self.close_button)


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Создание кнопки "Открыть второе окно"
        self.open_button = QPushButton('Открыть второе окно')
        self.open_button.clicked.connect(self.open_second_window)

        # Установка кнопки "Открыть второе окно" в главное окно
        self.setCentralWidget(self.open_button)

    def open_second_window(self):
        # Создание второго окна
        second_window = SecondWindow()
        second_window.setWindowTitle('Второе окно')
        second_window.setGeometry(100, 100, 200, 100)
        second_window.show()


if __name__ == '__main__':
    app = QApplication([])
    main_window = MainWindow()
    main_window.setWindowTitle('Главное окно')
    main_window.setGeometry(100, 100, 200, 100)
    main_window.show()
    app.exec()
