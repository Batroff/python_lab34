# БСБО-05-19 Савранский С.

def same_by(characteristic, objects):
    mapped = list(map(characteristic, objects))
    return len(mapped) == mapped.count(mapped[0])

