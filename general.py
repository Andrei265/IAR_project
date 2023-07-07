import sys

from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtSql import QSqlTableModel

from main_ui import Ui_MainWindow
from new_aircraft_ui import Ui_Dialog
from database import Data


class ExpenseTracker(QMainWindow):
    def __init__(self):
        super(ExpenseTracker, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.conn = Data()
        self.view_data()
        self.reload_data()
        
        self.ui.add_aircraft.clicked.connect(self.open_add_aircraft_window)

    def open_add_aircraft_window(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        sender = self.sender()
        if sender.text() == "Добавить ВС":
            self.ui_window.add_aircraft.clicked.connect(self.add_new_transaction)
        else:
            self.ui_window.add_aircraft.clicked.connect(self.edit_current_transaction)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ExpenseTracker()
    window.show()

    sys.exit(app.exec())