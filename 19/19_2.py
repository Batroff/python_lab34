# БСБО-05-19 Савранский С.

def char_to_int(ch):
    return {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8}.get(ch)


def int_to_char(i):
    return {1: 'A', 2: 'B', 3: 'C', 4: 'D', 5: 'E', 6: 'F', 7: 'G', 8: 'H'}.get(i)


def get_turns(x, y):
    return [(x - 1, y - 2), (x + 1, y - 2),
            (x - 2, y - 1), (x + 2, y - 1),
            (x - 2, y + 1), (x + 2, y + 1),
            (x - 1, y + 2), (x + 1, y + 2)]


def possible_turns(cell):
    x, y = char_to_int(cell[0]), int(cell[1])
    possible = [t for t in get_turns(x, y)
                if False not in [False for c in t if c < 1 or c > 8]]

    return sorted(map(lambda coord: f'{int_to_char(coord[0])}{coord[1]}', possible))


print(possible_turns("H8"))
