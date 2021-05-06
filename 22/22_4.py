# БСБО-05-19 Савранский С.

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


def solve(*coefficients):
    if len(coefficients) == 3:
        a, b, c = coefficients
        return roots_of_quadratic_equation(a, b, c)
    elif len(coefficients) == 2:
        b, c = coefficients
        return roots_of_quadratic_equation(0, b, c)
    elif len(coefficients) == 1:
        c = coefficients[0]
        return roots_of_quadratic_equation(0, 0, c)

    return None

