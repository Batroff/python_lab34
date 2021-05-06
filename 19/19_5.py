# БСБО-05-19 Савранский С.

def prime(number):
    return len([i for i in range(2, number) if number % i == 0]) == 0
