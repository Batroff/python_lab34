# БСБО-05-19 Савранский С.

import math

i = 0
calc_dist = lambda x, y: ((x - 0.75) ** 2 + (y - 0) ** 2) ** .5 
while i < 2 * math.pi:
    x = math.cos(i) ** 3
    y = math.sin(i) ** 3

    if i == 0:
        dist = calc_dist(x, y)
    elif (new_dist := calc_dist(x, y)) < dist:
        dist = new_dist
    i += .0001
