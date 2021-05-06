# БСБО-05-19 Савранский С.

def partial_sums(*args):
    return [sum(args[:i]) for i in range(len(args) + 1)]

