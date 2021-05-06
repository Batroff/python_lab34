# БСБО-05-19 Савранский С.

def equation(a, b):
    x1, y1 = [float(i) for i in a.split(';')]
    x2, y2 = [float(i) for i in b.split(';')]
    if y2 - y1 == 0 or x2 - x1 == 0:
        print(y1)
        return

    k = (y2 - y1) / (x2 - x1)
    b = y1
    print(f'{k} {b}')
