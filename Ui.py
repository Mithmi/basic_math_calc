# -*- coding: utf-8 -*-
import sys
from sympy import *
from PyQt4 import QtGui, QtCore
from Main import Lagrange, Silvester
x, y, z = symbols('x y z')
j0, j1, h1, h2 = var('j0 j1 h1 h2')

class SilvesterUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.input = QtGui.QLineEdit("Hello")
        btnCalc = QtGui.QPushButton("Рассчитать", self)
        btnCalc.setGeometry(150, 75, 200, 30)

        self.connect(btnCalc, QtCore.SIGNAL('clicked()'), self.get_text)
        self.update()

        info = self.get_text()
        lTitle = QtGui.QLabel(info, self)
        lTitle.setAlignment(QtCore.Qt.AlignHCenter)
        lTitle.setGeometry(100,10,300,20)


        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(btnCalc)
        layout.addWidget(lTitle)
        self.setLayout(layout)

    def get_text(self):
        insertedText = self.input.text()
        return insertedText


class LagrangeUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.input = QtGui.QLineEdit("Hello")
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.input)
        self.setLayout(layout)

class OptimizationUI(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.input = QtGui.QLineEdit("Hello")
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.input)
        self.setLayout(layout)

class MainWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.tabs = QtGui.QTabWidget(self)

        self.tabs.addTab(SilvesterUI(), 'Сильвестр')
        self.tabs.addTab(LagrangeUI(), 'Лагранж')
        self.tabs.addTab(OptimizationUI(), 'Оптимизация')
        layout = QtGui.QHBoxLayout()

        self.setGeometry(600, 300, 500, 450)
        self.setWindowTitle("Приложение для решения задач Методов Оптимизиации")
        self.setWindowIcon(QtGui.QIcon('data/crazy.ico'))

#        equation = x * y - 10
#        lag = Lagrange(func, equation)



#        lDescription = QtGui.QLabel(str(equation), self)
#        lDescription.setAlignment(QtCore.Qt.AlignHCenter)
#        lDescription.setGeometry(100, 35, 300, 40)

#        Description = QtGui.QLabel(str(lag), self)
#        Description.setAlignment(QtCore.Qt.AlignHCenter)
#        Description.setGeometry(100, 115, 300, 500)

#        btnCalc = QtGui.QPushButton("Рассчитать", self)
#        btnCalc.setGeometry(150, 75, 200, 30)
#        self.connect(btnCalc, QtCore.SIGNAL('clicked()'), quit)

#        layout.addWidget(lTitle)
        self.setLayout(QtGui.QVBoxLayout())
        self.layout().addWidget(self.tabs)

app = QtGui.QApplication(sys.argv)
tg = MainWidget()
tg.show()
app.exec()