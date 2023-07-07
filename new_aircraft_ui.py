# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_aircraft.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QLabel, QPushButton, QSizePolicy, QSpacerItem,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(503, 204)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"background-color: rgba(255, 255, 255, 30); \n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_aircraft = QLabel(self.frame)
        self.label_aircraft.setObjectName(u"label_aircraft")
        self.label_aircraft.setMinimumSize(QSize(0, 35))
        self.label_aircraft.setStyleSheet(u"color: white;")
        self.label_aircraft.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_aircraft)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.combo_add_aircraft = QComboBox(self.frame)
        self.combo_add_aircraft.addItem("")
        self.combo_add_aircraft.addItem("")
        self.combo_add_aircraft.setObjectName(u"combo_add_aircraft")
        self.combo_add_aircraft.setMinimumSize(QSize(0, 35))
        self.combo_add_aircraft.setStyleSheet(u"QComboBob {\n"
"font-size: 16pt;\n"
"color: white;\n"
"}\n"
"\n"
"QComboBox:item {\n"
"color: black;\n"
"}")
        self.combo_add_aircraft.setEditable(False)
        self.combo_add_aircraft.setMaxVisibleItems(10)
        self.combo_add_aircraft.setMaxCount(2147483647)
        self.combo_add_aircraft.setDuplicatesEnabled(False)

        self.verticalLayout.addWidget(self.combo_add_aircraft)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.add_aicraft_in = QPushButton(self.frame)
        self.add_aicraft_in.setObjectName(u"add_aicraft_in")
        self.add_aicraft_in.setMinimumSize(QSize(0, 35))
        self.add_aicraft_in.setStyleSheet(u"QPushButton{\n"
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

        self.verticalLayout.addWidget(self.add_aicraft_in)


        self.verticalLayout_3.addLayout(self.verticalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        self.combo_add_aircraft.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Add_aircraft", None))
        self.label_aircraft.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u043b\u0435\u043d\u0438\u0435 \u043d\u043e\u0432\u043e\u0433\u043e \u0412\u0421", None))
        self.combo_add_aircraft.setItemText(0, QCoreApplication.translate("Dialog", u"11", None))
        self.combo_add_aircraft.setItemText(1, QCoreApplication.translate("Dialog", u"2222", None))

        self.combo_add_aircraft.setCurrentText(QCoreApplication.translate("Dialog", u"11", None))
        self.add_aicraft_in.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0412\u0421", None))
    # retranslateUi

