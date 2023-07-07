# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QTextBrowser, QVBoxLayout,
    QWidget)
from PySide6.QtWebEngineWidgets import QWebEngineView

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(1865, 948)
        MainWindow.setMinimumSize(QSize(0, 0))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.Description = QTextBrowser(self.centralwidget)
        self.Description.setObjectName(u"Description")
        self.Description.setMaximumSize(QSize(340, 16777215))
        self.Description.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"color: white;\n"
"")

        self.verticalLayout.addWidget(self.Description)

        self.comboBox = QComboBox(self.centralwidget)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBob {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")

        self.verticalLayout.addWidget(self.comboBox)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.add_aircraft = QPushButton(self.centralwidget)
        self.add_aircraft.setObjectName(u"add_aircraft")
        self.add_aircraft.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_3.addWidget(self.add_aircraft)

        self.delete_aircraft = QPushButton(self.centralwidget)
        self.delete_aircraft.setObjectName(u"delete_aircraft")
        self.delete_aircraft.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_3.addWidget(self.delete_aircraft)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.avb = QPushButton(self.centralwidget)
        self.avb.setObjectName(u"avb")
        self.avb.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.verticalLayout.addWidget(self.avb)

        self.map = QPushButton(self.centralwidget)
        self.map.setObjectName(u"map")
        self.map.setStyleSheet(u"QPushButton{\n"
"	color: rgb(255, 255, 255);\n"
"     background-color:rgba(255,255,255,30);\n"
"     border: 1px solid rgba(255,255,255,40);\n"
"     border-radius:7px;\n"
"	height: 20;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color:rgba(255,255,255,70);\n"
"}")

        self.verticalLayout.addWidget(self.map)


        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.mmaapp = QWebEngineView()
        self.mmaapp.setObjectName(u"mmaapp")

        self.horizontalLayout_2.addWidget(self.mmaapp)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.aircraft_table = QTableWidget(self.centralwidget)
        if (self.aircraft_table.columnCount() < 8):
            self.aircraft_table.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.aircraft_table.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.aircraft_table.setObjectName(u"aircraft_table")
        self.aircraft_table.setMinimumSize(QSize(1000, 0))
        self.aircraft_table.setMaximumSize(QSize(16777215, 250))
        self.aircraft_table.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 7pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: 0pt;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.aircraft_table.setShowGrid(False)
        self.aircraft_table.horizontalHeader().setDefaultSectionSize(203)

        self.horizontalLayout.addWidget(self.aircraft_table)

        self.avb_table = QTableWidget(self.centralwidget)
        if (self.avb_table.columnCount() < 5):
            self.avb_table.setColumnCount(5)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.avb_table.setHorizontalHeaderItem(0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.avb_table.setHorizontalHeaderItem(1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.avb_table.setHorizontalHeaderItem(2, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.avb_table.setHorizontalHeaderItem(3, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.avb_table.setHorizontalHeaderItem(4, __qtablewidgetitem12)
        self.avb_table.setObjectName(u"avb_table")
        self.avb_table.setMaximumSize(QSize(16777215, 250))
        self.avb_table.setStyleSheet(u"QTableView {\n"
"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-bottom-right-radius: 7px; \n"
"border-bottom-left-radius: 7px; \n"
"color: white;\n"
"}\n"
"\n"
"QHeaderView::section {\n"
"background-color: rgb(53, 53, 53);\n"
"color: white;\n"
"border: none;\n"
"height: 50px;\n"
"font-size: 7pt;\n"
"}\n"
"\n"
"QTableView::item {\n"
"    border-style: none;\n"
"    border-bottom: 1px solid rgba(255,255,255,50);\n"
"    padding-left: 0pt;\n"
"    padding-right: auto;\n"
"}\n"
"\n"
"QTableView::item:selected{\n"
"	border: none;\n"
"	color: rgb(255, 255, 255);\n"
"    background-color: rgba(255, 255, 255, 50);\n"
"}")
        self.avb_table.setShowGrid(False)
        self.avb_table.horizontalHeader().setDefaultSectionSize(170)

        self.horizontalLayout.addWidget(self.avb_table)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Aircrafts", None))
        self.Description.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans SC'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">1) \u0414\u043e\u0431\u0430\u0432\u044c\u0442\u0435 \u0441\u0430\u043c\u043e\u043b\u0435\u0442\u044b \u0434\u043b\u044f \u0440\u0430\u0441\u0447\u0435\u0442\u0430.<br />2) \u0420\u0430\u0441\u0447\u0438\u0442\u0430\u0439\u0442\u0435 \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u044b\u0435 \u0410\u0432\u0411 \u0434\u043b\u044f \u0432\u0437\u043b\u0435\u0442\u0430 \u0438 \u043f\u043e\u0441\u0430\u0434\u043a\u0438.<br />3) \u041f\u043e\u0441\u0442\u0440\u043e\u0439\u0442\u0435 \u043a\u0430\u0440\u0442\u0443 \u0434"
                        "\u043b\u044f \u043e\u0442\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u044f \u0432\u043e\u0437\u043c\u043e\u0436\u043d\u043e\u0441\u0442\u0435\u0439 \u0412\u0421.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0416\u0435\u043b\u0442\u044b\u043c \u043a\u0440\u0443\u0433\u043e\u043c \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0434\u0438\u0443\u0441 \u043f\u043e\u043b\u0435\u0442\u0430 \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u043b\u0438 \u0433\u0440\u0443\u043f\u043f\u044b \u0412\u0421 \u0432 \u043e\u0434\u043d\u0443 \u0441\u0442\u043e\u0440\u043e\u043d\u0443.</span></p>\n"
"<p align=\"justify\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt;\">\u0417\u0435\u043b\u0435\u043d"
                        "\u044b\u043c \u043a\u0440\u0443\u0433\u043e\u043c \u043e\u0431\u043e\u0437\u043d\u0430\u0447\u0435\u043d \u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c\u043d\u044b\u0439 \u0440\u0430\u0434\u0438\u0443\u0441 \u043f\u043e\u043b\u0435\u0442\u0430 \u043e\u0434\u043d\u043e\u0433\u043e \u0438\u043b\u0438 \u0433\u0440\u0443\u043f\u043f\u044b \u0412\u0421 \u0432 \u043e\u0431\u0435 \u0441\u0442\u043e\u0440\u043e\u043d\u044b.</span></p></body></html>", None))
        self.add_aircraft.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0412\u0421", None))
        self.delete_aircraft.setText(QCoreApplication.translate("MainWindow", u"\u0423\u0434\u0430\u043b\u0438\u0442\u044c \u0412\u0421", None))
        self.avb.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0447\u0435\u0442 \u0410\u0432\u0411", None))
        self.map.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u0442\u0440\u043e\u0438\u0442\u044c \u043a\u0430\u0440\u0442\u0443", None))
        ___qtablewidgetitem = self.aircraft_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0412\u0421", None));
        ___qtablewidgetitem1 = self.aircraft_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0440\u0430\u0437\u0431\u0435\u0433\u0430", None));
        ___qtablewidgetitem2 = self.aircraft_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u043f\u0440\u043e\u0431\u0435\u0433\u0430", None));
        ___qtablewidgetitem3 = self.aircraft_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"\u041c\u0430\u043a\u0441. \u0432\u0437\u043b\u0435\u0442\u043d\u0430\u044f \u043c\u0430\u0441\u0441\u0430", None));
        ___qtablewidgetitem4 = self.aircraft_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b-\u0442\u044c \u043f\u043e\u043b\u0435\u0442\u0430 \u043d\u0435 \u0441\u043d\u0430\u0440-\u0433\u043e \u0432 1 \u0441\u0442-\u043d\u0443", None));
        ___qtablewidgetitem5 = self.aircraft_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b-\u0442\u044c \u043f\u043e\u043b\u0435\u0442\u0430 \u0441\u043d\u0430\u0440-\u0433\u043e \u0432 1 \u0441\u0442-\u043d\u0443", None));
        ___qtablewidgetitem6 = self.aircraft_table.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b-\u0442\u044c \u043f\u043e\u043b\u0435\u0442\u0430 \u043d\u0435 \u0441\u043d\u0430\u0440-\u0433\u043e \u0432 2 \u0441\u0442-\u043d\u044b", None));
        ___qtablewidgetitem7 = self.aircraft_table.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"\u0414\u0430\u043b-\u0442\u044c \u043f\u043e\u043b\u0435\u0442\u0430 \u0441\u043d\u0430\u0440-\u0433\u043e \u0432 2 \u0441\u0442-\u043d\u044b", None));
        ___qtablewidgetitem8 = self.avb_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0410\u0432\u0411", None));
        ___qtablewidgetitem9 = self.avb_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043b\u0438\u043d\u0430 \u0412\u041f\u041f", None));
        ___qtablewidgetitem10 = self.avb_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"\u041a\u043b\u0430\u0441\u0441 \u0412\u041f\u041f", None));
        ___qtablewidgetitem11 = self.avb_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"\u0414\u043e\u043b\u0433\u043e\u0442\u0430", None));
        ___qtablewidgetitem12 = self.avb_table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"\u0428\u0438\u0440\u043e\u0442\u0430", None));
    # retranslateUi

