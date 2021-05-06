# БСБО-05-19 Савранский С.

def palindrome(s):
    res = ''.join(s.lower().split(' '))
    return 'Палиндром' if res == res[::-1] else 'Не палиндром'
