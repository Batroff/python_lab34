# БСБО-05-19 Савранский С.

def line(s, t):
    k, b = [float(i) for i in s.split('x')]
    x, y = [float(i) for i in t.split(';')]
    print('True' if y == k * x + b else 'False')
