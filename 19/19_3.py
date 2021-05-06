# БСБО-05-19 Савранский С.
from math import sqrt


def roots_of_quadratic_equation(a, b, c):
    if a == 0:
        return [- c / b]

    d = b ** 2 - 4 * a * c
    if d < 0:
        return ['all']
    elif d == 0:
        return [(-b - sqrt(d)) / (2 * a)]

    x1 = (-b - sqrt(d)) / (2 * a)
    x2 = (-b + sqrt(d)) / (2 * a)
    return [x1, x2]


print(*sorted(roots_of_quadratic_equation(1, -3, 2)))
