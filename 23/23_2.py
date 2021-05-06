# БСБО-05-19 Савранский С.

from math import pi

def find_farthest_orbit(list_of_orbits):
    s = lambda x: x[0] * x[1] * pi
    max_s = max(s(x) for x in orbits if x[0] != x[1])
    return [x for x in orbits if s(x) == max_s][0]

