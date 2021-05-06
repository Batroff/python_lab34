# БСБО-05-19 Савранский С.

def transpose(matrix):
    matrix[:] = [list(x) for x in zip(*matrix)]
