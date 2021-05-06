# БСБО-05-19 Савранский С.

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, b + a
    return a


def golden_ratio(i):
    return fibonacci(i + 1) / fibonacci(i)
