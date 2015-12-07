import string
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
x, y, z = symbols('x y z')
j0, j1, h1, h2 = var('j0 j1 h1 h2')


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
    for k in range(len(result)):
        m1 = minor1.evalf(subs={x: result[k][x]})
        m2 = minor2.evalf(subs={x: result[k][x]})
        m3 = minor3.evalf(subs={x: result[k][x]})
        if m1 >= 0 and m2 >= 0 and m3 >= 0:
            matrix_status = "matrix >= 0"
            print(matrix_status)
            print("X - locmin")
        elif m1 <= 0 and m2 >= 0 and m3 <= 0:
            matrix_status = "matrix <= 0"
            print(matrix_status)
            print("X - locmin")
        else:
            matrix_status = "matrix unindentified"
            print(matrix_status)
            print("X - isn't locextrm")

def OptimizationDeter(func):
    m = 0
    done = False
    while not done:
        dx = diff(func, x, m)
        print(dx)
        check = dx.evalf(subs={x:0})
        print(check)
        print(m)
        if check != 0:
            return m
        else:
            m += 1
    return m

def Lagrange(func, equation):
    j0 = 1
    L = j0*(func) + j1*(equation)
    Lx = diff(L, x)
    Ly = diff(L, y)
    print(Lx, '\n', Ly, '\n', equation)
    calc = solve([Lx, Ly, equation])
    print(calc)
    LM = Matrix(((diff(Lx, x), diff(Lx, y)), (diff(Ly, x), diff(Ly, y))))
    print(LM)
    H = h1 * diff(equation, x) + h2 * diff(equation, y)
    print(H)
    result = solve(H, h1)
    print(result)
    LH = h1**2 + 2*h1*h2 + h2**2
    for i in range(len(calc)):
        j = calc[i][j1]
        minor1 = LM[0, 0].evalf(subs={j1:j})
        minor2 = LM.det().evalf(subs={j1:j})
        print(minor1, minor2, j)
        y1 = calc[i][y]
        x1 = calc[i][x]
        print(y1, x1, x1/y1)
        for k in range(len(result)):
            print('x ==', x1, 'y ==', y1)
            results = result[k].subs({x:x1, y:y1})
            print(results)
            LH = LH.subs({h1:results})
            print(LH)
            Result = LH.subs({h2:1})
            print(Result)
            if Result > 0:
                print('local minimum')
            elif Result < 0:
                print('local maximum')
            else:
                print('not extremum')
    answer = str(Lx) + '\n' + str(Ly) + '\n' +  str(equation) +  '\n' +  '-'*10 +  '\n' + str(calc) + '\n' + '-'*10 + '\n' + str(latex(LM)) + '\n' + str(minor1) + '\n' + str(minor2) + '\n' + str(j) + '\n' + str(H)
    return answer

def main():
    allowed = "0123456789+-/*xyzcosintgqrab()"
    task = input('Silv, Opti or Lag?')
    if task == 'Silv':
        try:
            func = str(parse_expr(input('Give me function')))
            #func = "x**3 + y**2 + 0 * z**2 + y * z * 0 - 3 * x + 6 * y + 2"
            result = filter(func, allowed)
            print('func: ', result)
            Silv = Silvester(result)
        except (TypeError, ValueError):
            print('Error')
    elif task == 'Opti':
        try:
            func = str(parse_expr(input('Give me function')))
            result = filter(func, allowed)
            #func = "sin(x) * (-x)**5"
            print('func: ', result)
            Opti = OptimizationDeter(result)
        except (TypeError, ValueError):
            print('Error')
    elif task == 'Lag':
        try:
            func = str(parse_expr(input('Give me function')))
            equation = str(parse_expr(input('Give me Equation')))
            result = filter(func, allowed)
            result1 = filter(equation, allowed)
            #func = "5 * x**2 + y**2 + 2 * x * y"
            #equation = "x * y - 10"
            print('func: ', result, '\n', 'equation: ', result1)
            Lag = Lagrange(result, result1)
        except (TypeError, ValueError):
            print('Error')


if __name__ == "__main__":
    main()