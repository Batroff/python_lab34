# БСБО-05-19 Савранский С.

def defractalize(arr):
    res = [i for i in arr if i is not arr]
    arr.clear()
    arr.extend(res)
