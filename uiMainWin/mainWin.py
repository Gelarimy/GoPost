# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPalette, QColor

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1454, 590)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget_sender = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_sender.setGeometry(QtCore.QRect(20, 90, 611, 391))
        self.tableWidget_sender.setObjectName("tableWidget_sender")
        self.tableWidget_sender.setColumnCount(0)
        self.tableWidget_sender.setRowCount(0)
        self.radioButton_a5 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_a5.setGeometry(QtCore.QRect(690, 230, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.radioButton_a5.setFont(font)
        self.radioButton_a5.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_a5.setObjectName("radioButton_a5")
        self.tableWidget_receiver = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_receiver.setGeometry(QtCore.QRect(820, 90, 611, 391))
        self.tableWidget_receiver.setObjectName("tableWidget_receiver")
        self.tableWidget_receiver.setColumnCount(0)
        self.tableWidget_receiver.setRowCount(0)
        self.sender = QtWidgets.QLabel(self.centralwidget)
        self.sender.setGeometry(QtCore.QRect(240, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.sender.setFont(font)
        self.sender.setTextFormat(QtCore.Qt.RichText)
        self.sender.setObjectName("sender")
        self.receiver = QtWidgets.QLabel(self.centralwidget)
        self.receiver.setGeometry(QtCore.QRect(1070, 10, 151, 21))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.receiver.setFont(font)
        self.receiver.setTextFormat(QtCore.Qt.RichText)
        self.receiver.setObjectName("receiver")
        self.radioButton_a6 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_a6.setGeometry(QtCore.QRect(690, 260, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.radioButton_a6.setFont(font)
        self.radioButton_a6.setIconSize(QtCore.QSize(30, 30))
        self.radioButton_a6.setObjectName("radioButton_a6")
        self.pushButton_print = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_print.setGeometry(QtCore.QRect(680, 310, 101, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.pushButton_print.setFont(font)
        self.pushButton_print.setObjectName("pushButton_print")
        self.pushButton_add_sender = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_sender.setGeometry(QtCore.QRect(160, 490, 231, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.pushButton_add_sender.setFont(font)
        self.pushButton_add_sender.setObjectName("pushButton_add_sender")
        self.pushButton_add_receiver = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_add_receiver.setGeometry(QtCore.QRect(1020, 490, 221, 41))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.pushButton_add_receiver.setFont(font)
        self.pushButton_add_receiver.setObjectName("pushButton_add_receiver")
        self.lineEdit_sender = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_sender.setGeometry(QtCore.QRect(20, 50, 521, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.lineEdit_sender.setFont(font)
        self.lineEdit_sender.setObjectName("lineEdit_sender")
        self.choose_sender = QtWidgets.QPushButton(self.centralwidget)
        self.choose_sender.setGeometry(QtCore.QRect(544, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.choose_sender.setFont(font)
        self.choose_sender.setObjectName("choose_sender")
        self.pushButton_sended = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_sended.setGeometry(QtCore.QRect(650, 380, 151, 51))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.pushButton_sended.setFont(font)
        self.pushButton_sended.setObjectName("pushButton_sended")
        self.lineEdit_receiver = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_receiver.setGeometry(QtCore.QRect(820, 50, 511, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.lineEdit_receiver.setFont(font)
        self.lineEdit_receiver.setObjectName("lineEdit_receiver")
        self.choose_receiver = QtWidgets.QPushButton(self.centralwidget)
        self.choose_receiver.setGeometry(QtCore.QRect(1344, 50, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Cambria")
        font.setPointSize(14)
        self.choose_receiver.setFont(font)
        self.choose_receiver.setObjectName("choose_receiver")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1454, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.radioButton_a5.setText(_translate("MainWindow", "A 5"))
        self.sender.setText(_translate("MainWindow", "Отправитель"))
        self.receiver.setText(_translate("MainWindow", "Получатель"))
        self.radioButton_a6.setText(_translate("MainWindow", "A 6"))
        self.pushButton_print.setText(_translate("MainWindow", "Печать"))
        self.pushButton_add_sender.setText(_translate("MainWindow", "Добавить отправителя"))
        self.pushButton_add_receiver.setText(_translate("MainWindow", "Добавить получателя"))
        self.choose_sender.setText(_translate("MainWindow", "Выбрать"))
        self.pushButton_sended.setText(_translate("MainWindow", "Отправленные"))
        self.choose_receiver.setText(_translate("MainWindow", "Выбрать"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
