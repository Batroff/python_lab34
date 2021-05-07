# БСБО-05-19 Савранский С.
from re import split
print(any([True for i in split('\s|\n', input('matrix >> ')) if int(i) == 0]))
