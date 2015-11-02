from sympy import *


def Silvester(func):
    dx = diff(func, x)
    dy = diff(func, y)
    dz = diff(func, z)
    print(dx, dy, dz)
    result = solve([dx, dy, dz], [x, y, z])
    print(result)

    dxx = diff(dx, x)
    dxy = diff(dx, y)
    dxz = diff(dx, z)

    dyx = diff(dy, x)
    dyy = diff(dy, y)
    dyz = diff(dy, z)

    dzx = diff(dz, x)
    dzy = diff(dz, y)
    dzz = diff(dz, z)

    M = Matrix([[dxx, dxy, dxz], [dyx, dyy, dyz], [dzx, dzy, dzz]])
    N = Matrix([[dxx, dxy], [dyx, dyy]])
    print(M)
    minor1 = M[0, 0]
    minor2 = N.det()
    minor3 = M.det()
    m1 = minor1.evalf(subs={x: result[0][0]})
    m2 = minor2.evalf(subs={x: result[0][0]})
    m3 = minor3.evalf(subs={x: result[0][0]})
    print(m1, m2, m3)
    if m1 >= 0 and m2 >= 0 and m3 >= 0:
        matrix_status = "matrix >= 0"
        print(matrix_status)
        return print("X - locmin")
    elif m1 <= 0 and m2 >= 0 and m3 <= 0:
        matrix_status = "matrix <= 0"
        print(matrix_status)
        return print("X - locmin")
    else:
        matrix_status = "matrix unindentified"
        print(matrix_status)
        return print("X - isn't locextrm")

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

x, y, z = symbols('x y z')
func = x ** 3 + y ** 2 + z ** 2 + y * z - 3 * x + 6 * y + 2
Silv = Silvester(func)
func = sin(x) * (-x) ** 5
Opti = OptimizationDeter(func)
