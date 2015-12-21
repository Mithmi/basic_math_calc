# -*- coding: utf-8 -*-
import string
import sys
from sympy import *
from sympy.parsing.sympy_parser import parse_expr, stringify_expr
from PyQt4 import QtCore, QtGui, uic
form_class = uic.loadUiType("GuiManita.ui")[0]
x, y, z = symbols('x y z')
j0, j1, h1, h2 = var('j0 j1 h1 h2')

class MyWindowClass(QtGui.QMainWindow, form_class):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self,parent)
        self.allowed = "0123456789+-/*xyzcosintgqrab()"
        self.setupUi(self)
        self.pushButton.clicked.connect(self.Silv_button_clicked)
        self.pushButton_2.clicked.connect(self.Opti_button_clicked)
        self.pushButton_3.clicked.connect(self.Lag_button_clicked)
        self.scrollArea_3.setWidget(self.label_6)


    def Silv_button_clicked(self):
        value = self.lineEdit.text()
        reforged = filter(value, self.allowed)
        self.label.setText(reforged)
        Silv = Silvester(reforged)
        self.label_2.setText(Silv)

    def Opti_button_clicked(self):
        value = self.lineEdit_2.text()
        reforged = filter(value, self.allowed)
        self.label_3.setText(reforged)
        Opti = OptimizationDeter(reforged)
        self.label_4.setText(Opti)

    def Lag_button_clicked(self):
        value = self.lineEdit_3.text()
        value1 = self.lineEdit_4.text()
        reforged = filter(value, self.allowed)
        reforged1 = filter(value1, self.allowed)
        self.label_5.setText(reforged)
        self.label_7.setText(reforged1)
        Lag = Lagrange(reforged, reforged1)
        self.label_6.setText(Lag)


def fmtstr(fmt, str):
    res = [];
    i = 0;
    for c in fmt:
        if c == '#':
            res.append(str[i:i+1]); i = i+1;
        else:
            res.append(c)
    res.append(str[i:])
    return string.join(res)

def filter(inStr, allowed):
    outStr = ''
    for c in inStr:
        if c in allowed:
            outStr += c
    return outStr

def Silvester(func):
    result = ""
    dx = diff(func, x)
    dy = diff(func, y)
    dz = diff(func, z)
    result = solve([dx, dy, dz], [x, y, z])
    que = [x, y, z]
    dque = [dx, dy, dz]
    res = []
    for i in range(len(que)):
        for j in range(len(que)):
            d = diff(dque[i], que[j])
            res.append(d)
    M = Matrix([res[0:3], res[3:6], res[6:9]])
    N = Matrix([res[0:2], res[3:5]])
    minor1 = M[0, 0]
    minor2 = N.det()
    minor3 = M.det()
    N = Matrix([res[4:6], res[7:9]])
    minor4 = N.det()
    N = Matrix([[res[0], res[2]], [res[7], res[8]]])
    minor5 = N.det()
    minor6 = res[8]
    minor7 = res[4]
    minor8 = res[0]
    hart = ""
    for k in range(len(result)):
        try:
            m1 = minor1.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m2 = minor2.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m3 = minor3.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m4 = minor3.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m5 = minor3.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m6 = minor3.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m7 = minor3.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            m8 = minor3.evalf(subs={x: result[k][x], y: result[k][y], z: result[k][z]})
            hart += "x = " + str(result[k][x]) + "\n" \
                + "y = " + str(result[k][y]) + "\n" \
                + "z = " + str(result[k][z]) + "\n\n"
        except KeyError:
            try:
                m1 = minor1.evalf(subs={x: result[k][x], y: result[k][y]})
                m2 = minor2.evalf(subs={x: result[k][x], y: result[k][y]})
                m3 = minor3.evalf(subs={x: result[k][x], y: result[k][y]})
                m4 = minor3.evalf(subs={x: result[k][x], y: result[k][y]})
                m5 = minor3.evalf(subs={x: result[k][x], y: result[k][y]})
                m6 = minor3.evalf(subs={x: result[k][x], y: result[k][y]})
                m7 = minor3.evalf(subs={x: result[k][x], y: result[k][y]})
                m8 = minor3.evalf(subs={x: result[k][x], y: result[k][y]})
                hart += "x = " + str(result[k][x]) + "\n" \
                + "y = " + str(result[k][y]) + "\n" \
                + "z = " + "0" + "\n\n"
            except KeyError:
                m1 = minor1.evalf(subs={x: result[k][x]})
                m2 = minor2.evalf(subs={x: result[k][x]})
                m3 = minor3.evalf(subs={x: result[k][x]})
                m4 = minor3.evalf(subs={x: result[k][x]})
                m5 = minor3.evalf(subs={x: result[k][x]})
                m6 = minor3.evalf(subs={x: result[k][x]})
                m7 = minor3.evalf(subs={x: result[k][x]})
                m8 = minor3.evalf(subs={x: result[k][x]})
                hart += "x = " + str(result[k][x]) + "\n" \
                + "y = " + "0" + "\n" \
                + "z = " + "0" + "\n\n"

        if m1 >= 0 and m2 >= 0 and m3 >= 0:
            matrix_status = "Так как все миноры >= 0, следовательно матрица >= 0"
            end = "А значит X точка - locmin, так как матрица - неотрицательно определена"
        elif m1 <= 0 and m2 >= 0 and m3 <= 0:
            matrix_status = "Так как некоторые из миноров >= 0, следовательно матрица =< 0"
            end = "А значит точка X - locmax, так как матрица - неположительно определена"
        elif m1 > 0 and m2 > 0 and m3 > 0:
            matrix_status = "Так как все миноры > 0, следовательно матрица > 0"
            end = "А значит точка X - locmin, так как матрица - положительно определена"
        elif m1 < 0 and m2 < 0 and m3 < 0:
            matrix_status = "Так как М1 все миноры < 0, следовательно матрица < 0"
            end = "А значит точка X - locmax, так как матрица - отрицательно определена"
        else:
            matrix_status = "Так как присутствуют Миноры > и < 0, то матрица является знакопеременной"
            end = "А значит точка X - не является locextrm"
    result = "Возьмём производную первого порядка по всем переменным:\n\n" \
    + "df/dx = " + str(dx) + "\n" \
    + "df/dy = " + str(dy) + "\n" \
    + "df/dz = " + str(dz) + "\n\n" \
    + "Решим уравнение вида df/d = 0:" + "\n\n" \
    + str(dx) + " =  0" + "\n" \
    + str(dy) + " =  0" + "\n" \
    + str(dz) + " =  0" + "\n\n" \
    + "Отсюда следует что:\n\n" \
    + hart \
    + "Построим матрицу производных второго порядка:" + "\n\n" \
    + str(res[0:3]) + "\n" \
    + str(res[3:6]) + "\n" \
    + str(res[6:9]) + "\n\n" \
    + "Вычисляем угловые миноры:\n\n" \
    + "M1 = " + str(minor1) + " = " + str(m1) + "\n" \
    + "M2 = " + str(minor2) + " = " + str(m2) + "\n" \
    + "M3 = " + str(minor3) + " = " + str(m3) + "\n" \
    + "M4 = " + str(minor4) + " = " + str(m4) + "\n" \
    + "M5 = " + str(minor5) + " = " + str(m5) + "\n" \
    + "M6 = " + str(minor6) + " = " + str(m6) + "\n" \
    + "M7 = " + str(minor7) + " = " + str(m7) + "\n" \
    + "M8 = " + str(minor8) + " = " + str(m8) + "\n\n" \
    + matrix_status + "\n" + end + "\n"
    return result


def OptimizationDeter(func):
    m = 0
    result = "Для решения данной задачи оптимизации необходимо брать" \
             " производные от функции до тех пор пока f`(x) =/= 0. \n\n"
    done = False
    while not done:
        dx = diff(func, x, m)
        check = dx.evalf(subs={x:0})
        result += "dx" + str(m) + " = " + str(dx) + " = " + str(check) + "\n"
        if check != 0:
            if m % 2 == 0:
                if check > 0:
                    result += "m = " + str(m) + " - четное следовательно точка Х " \
                                                "- locextrm, т.к. f`(X) > 0, то Х - locmin"
                else:
                    result += "m = " + str(m) + " - четное следовательно точка Х " \
                                                "- locextrm, т.к. f`(X) < 0, то Х - locmax"
            else:
                result += "m = " + str(m) + " - нечетное, нет экстремумов."
            return result
        else:
            m += 1
    return result

def Lagrange(func, equation):
    answer = "Составим функцию Лагранжа:\n"
    j0 = 1
    L = j0*parse_expr(func) + j1*parse_expr(equation)
    answer += "L(x,y,j0,j1) = " + str(L) + "\n\n" + "Возьмем производные первого порядка по всем переменным\n"
    Lx = diff(L, x)
    Ly = diff(L, y)
    calc = solve([Lx, Ly, equation])
    LM = Matrix(((diff(Lx, x), diff(Lx, y)), (diff(Ly, x), diff(Ly, y))))
    H = h1 * diff(equation, x) + h2 * diff(equation, y)
    result = solve(H, h1)
    LH = h1**2 + 2*h1*h2 + h2**2
    answer += "Lx = " + str(Lx) + "\n" + \
              "Ly = " + str(Ly) + "\n\n" + "Получаем систему уравнений:\n" \
              + str(Lx) + " = 0" + '\n' + str(Ly) + " = 0" + '\n' + str(equation) + " = 0" + '\n\n'
    answer += "Получаем следующие корни:\n"
    for i in range(len(calc)):
        j = calc[i][j1]
        minor1 = LM[0, 0].evalf(subs={j1:j})
        minor2 = LM.det().evalf(subs={j1:j})
        y1 = calc[i][y]
        x1 = calc[i][x]
        answer += "j = " + str(j) + "\n" + "y = " + str(y1) + "\n" + "x = " + str(x1) + "\n\n"
        if minor1 >= 0 and minor2 >= 0:
            matrix_status = "Так как все миноры >= 0, следовательно матрица >= 0"
            end = "А значит X точка - locmin, так как матрица - неотрицательно определена"
        elif minor1 <= 0 and minor2 >= 0:
            matrix_status = "Так как некоторые из миноров >= 0, следовательно матрица =< 0"
            end = "А значит точка X - locmax, так как матрица - неположительно определена"
        elif minor1 > 0 and minor2 > 0:
            matrix_status = "Так как все миноры > 0, следовательно матрица > 0"
            end = "А значит точка X - locmin, так как матрица - положительно определена"
        elif minor1 < 0 and minor2 < 0:
            matrix_status = "Так как М1 все миноры < 0, следовательно матрица < 0"
            end = "А значит точка X - locmax, так как матрица - отрицательно определена"
        else:
            matrix_status = "Так как присутствуют Миноры > и < 0, то матрица является знакопеременной"
            end = "А значит точка X - не является locextrm"
        answer += "Составим матрицу производных второго порядка:\n" + str(LM[0:2])\
              + "\n" + str(LM[2:4]) + "\n\n" + "m1 = " + str(minor1) + "\n" + "m2 = " + str(minor2)\
              + "\n\n" + str(matrix_status) + "\n" + str(end) + "\n\n" + "Составим LH:\n" + "LH = "\
              + str(H) + " = " + str(LH) + " = "
        for k in range(len(result)):
            results = result[k].subs({x:x1, y:y1})
            LH = LH.subs({h1:results})
            Result = LH.subs({h2:1})
            if Result > 0:
                answer += str(Result) + '\nТак как LH > 0 - local minimum\n\n'
            elif Result < 0:
                answer += str(Result) + '\nТак как LH < 0 - local maximum\n\n'
            else:
                answer += "\nНе является экстремумом\n\n"
    return answer

def main():
    #func = "x**3 + y**2 + 0 * z**2 + y * z * 0 - 3 * x + 6 * y + 2"
    #func = "sin(x) * (-x)**5"
    #func = "5 * x**2 + y**2 + 2 * x * y"
    #equation = "x * y - 10"
    app = QtGui.QApplication(sys.argv)
    myWindow = MyWindowClass(None)
    myWindow.show()
    app.exec_()


if __name__ == '__main__':
    main()