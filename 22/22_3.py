# БСБО-05-19 Савранский С.

scoring = {
            "Яблочко": 50,
            "Зеленое кольцо": 25,
            "Внешнее кольцо": {
                1: 8,
                2: 6,
                3: 42,
                # ...
                20: 50,
            },
            "Внутреннее кольцо": {
                1: 2,
                2: 9,
                3: 56,
                # ...
                20: 3,
            },
        }


def score(cell, num=None):
    return scoring.get(cell, "Error") if num is None else scoring.get(cell).get(num)

