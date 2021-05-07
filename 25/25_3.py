# БСБО-05-19 Савранский С.

import random


def monte_carlo(points, acc_exp):
    in_circle = 0
    cache = dict()

    def _rand_val(accuracy):
        return random.randint(0, accuracy) / accuracy
    
    def _get_else_add_in_cache(key):
        if hasattr(cache, str(key)):
            return cache.get(str(key))
        else:
            val = key ** 2
            cache[str(key)] = val
            return val

    def _is_in_circle(x, y, r):
        sqr_x = _get_else_add_in_cache(x)
        sqr_y = _get_else_add_in_cache(y)

        return (sqr_x + sqr_y) ** 0.5 < r

    acc = 10 ** acc_exp
    for i in range(points):
        x = _rand_val(acc)
        y = _rand_val(acc)
        
        if _is_in_circle(x, y, 1):
            in_circle += 1
    
    pi = in_circle / points * 4
    return pi


print(monte_carlo(1000000, 10))
