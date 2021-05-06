# БСБО-05-19 Савранский С.

def from_string_to_list(string, container):
    container.append(' '.join(string.split(' ')))


a = [1, 2, 3]
from_string_to_list("4 5 6", a)
print(*a)
