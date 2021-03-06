# БСБО-05-19 Савранский С.
from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0:
        return ['all'] if c == 0 else None
    elif a == 0:
        return [- c / b]

    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return [(-b - d**.5) / (2 * a)]

    x1 = (-b - d**.5) / (2 * a)
    x2 = (-b + d**.5) / (2 * a)
    return [x1, x2]


print(*sorted(roots_of_quadratic_equation(1, -3, 2)))
