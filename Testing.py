from sympy import *
from sympy.mpmath import *
import re

x, y, z, a = symbols('x y z a')
j0, j1, h1, h2 = var('j0 j1 h1 h2')
def fetch_input():
    userInput = input('number: ')
    try:
        return int(userInput)
    except ValueError:
        return s.var(userInput)

def twice():
    num = fetch_input()
    return 2*num






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



def change(inStr):
    outStr = ''
    for c in inStr:
        outStr += "#"
    return outStr


func = "5 * x**2 + y**2 + 2 * x * y"
func1 = "5*x**2+y**2+2*x*y!!"
"""

equation = x * y - 10
#Lag = Lagrange(func, equation)

m = diff(-2*x/a**2, x)
print(m)
f = (x - a/3)**2 * 2/a**2 * (a - x) * x
res = integrate(f, (x, 0, a))
print(res)

"""




