# БСБО-05-19 Савранский С.

inp = []
while i := input('Line >> '):
    inp.append(i)

print(*(f'Line {inp.index(line) + 1}: {line.lstrip()[2:]}\n' for line in inp if '#' in line))
