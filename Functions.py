import math
def f(x):
    return pow(x, 3) + x + 2


def derived_f(x):
    return 3*pow(x, 2) + 1


def second_derived_f(x):
    return 6*x


def g(x):
    return pow(x, 2) - 2


def derived_g(x):
    return 2*x


def second_derived_g(x):
    return 2


def z(x):
    return 2*x + 1


def derived_z(x):
    return 2


def second_derived_z(x):
    return 0


def s(x):
    return 3*pow(x, 2) + 1


def s_y(y):
    if (y-1)/3 < 0:
        return - math.sqrt(abs((y-1)/3))
    return math.sqrt((y-1)/3)


def derived_s_x(x):
    return 6*x


def derived_s_y(y):
    return 0


def sin(x):
    return 6*math.sin(x)


def sin_y(y):
    if -6 <= y <= 6:
        return math.asin(y/6)
    return "*"


def derived_sin_y(y):
    if -pow(y, 2) + 1 < 0:
        return"*"
    return 1/math.sqrt(-pow(y, 2) + 1)


def derived_sin_x(x):
    return 0


def minus_s(x):
    return -3*pow(x, 2)+1


def minus_s_y(y):
    if (y-1)/(-3) < 0:
        return - math.sqrt(abs((y-1)/(-3)))
    return math.sqrt((y-1)/(-3))


def derived_minus_s_y(y):
    if -y/3 + 1/3 < 0:
        return"*"
    return 1/(-6*math.sqrt(-y/3 + 1/3))


def derived_minus_s_x(x):
    return 0


def cube(x):
    try:
        return 3*pow(x, 3)
    except:
        return "*"


def cube_y(y):
    return 3*pow(y, 1/3)


def derived_cube_x(x):
    return 9*pow(x, 2)
