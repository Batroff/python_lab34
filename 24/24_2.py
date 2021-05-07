# БСБО-05-19 Савранский С.

gem = dict()
while inp := input('Word >> '):
    gem[inp] = sum([(ord(ch) - ord('A') + 1) for ch in inp.upper()])

print(*(f'{k}\n' for (k, v) in sorted(gem.items(), key=lambda x: x[1])))

