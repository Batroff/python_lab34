# БСБО-05-19 Савранский С.

def catalan(n):
    if n == 0:
        return 1

    return sum([catalan(i) * catalan(n - i - 1) for i in range(n)])
