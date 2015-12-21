# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GuiManita.ui'
#
# Created: Mon Dec 21 12:37:00 2015
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1067, 1732)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 1061, 1991))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(170, 10, 171, 21))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 60, 1001, 1991))
        self.label_2.setText(_fromUtf8(""))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pushButton = QtGui.QPushButton(self.tab)
        self.pushButton.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.lineEdit_2 = QtGui.QLineEdit(self.tab_3)
        self.lineEdit_2.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.lineEdit_2.setObjectName(_fromUtf8("lineEdit_2"))
        self.label_3 = QtGui.QLabel(self.tab_3)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 171, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(self.tab_3)
        self.label_4.setGeometry(QtCore.QRect(20, 60, 1001, 1991))
        self.label_4.setText(_fromUtf8(""))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.pushButton_2 = QtGui.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.lineEdit_3 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_3.setGeometry(QtCore.QRect(10, 10, 151, 20))
        self.lineEdit_3.setObjectName(_fromUtf8("lineEdit_3"))
        self.label_5 = QtGui.QLabel(self.tab_2)
        self.label_5.setGeometry(QtCore.QRect(170, 10, 171, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.tab_2)
        self.label_6.setGeometry(QtCore.QRect(20, 90, 1001, 1991))
        self.label_6.setText(_fromUtf8(""))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lineEdit_4 = QtGui.QLineEdit(self.tab_2)
        self.lineEdit_4.setGeometry(QtCore.QRect(10, 40, 151, 20))
        self.lineEdit_4.setObjectName(_fromUtf8("lineEdit_4"))
        self.label_7 = QtGui.QLabel(self.tab_2)
        self.label_7.setGeometry(QtCore.QRect(170, 40, 171, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.pushButton_3 = QtGui.QPushButton(self.tab_2)
        self.pushButton_3.setGeometry(QtCore.QRect(270, 10, 75, 23))
        self.pushButton_3.setObjectName(_fromUtf8("pushButton_3"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1991, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Решение задач Методов Оптимизации", None))
        self.label.setText(_translate("MainWindow", "Inserted Equation", None))
        self.pushButton.setText(_translate("MainWindow", "Рассчитать", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Критерий Сильвестра", None))
        self.label_3.setText(_translate("MainWindow", "Inserted Equation", None))
        self.pushButton_2.setText(_translate("MainWindow", "Рассчитать", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Оптимизация", None))
        self.label_5.setText(_translate("MainWindow", "Inserted Equation", None))
        self.label_7.setText(_translate("MainWindow", "Inserted Equation", None))
        self.pushButton_3.setText(_translate("MainWindow", "Рассчитать", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Метод Лагранжа", None))
