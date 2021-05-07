# БСБО-05-19 Савранский С.

import random
import re

def generate_password(m):
    symbols = 'asdfghjklqwertyuipzxcvbnm23456789'
    def _generator():
        res = ''

        while len(res) < m:
            ch = symbols[random.randint(0, len(symbols) - 1)]
            if ch == 'l':
                res += 'L'
            elif ch == 'i':
                res += 'i'
            else:
                res += ch.upper() if random.randint(0, 1) == 1 else ch
        return res
    
    def _check(p):
        if len(re.findall('[a-z]', p)) == 0 \
                or len(re.findall('[A-Z]', p)) == 0 \
                or len(re.findall('[0-9]', p)) == 0:
                    return False
        return True
    
    res = ''
    while True:
        res = _generator()
        if _check(res):
            break
        
    return res


def main(n, m):
    return [generate_password(m) for _ in range(n)]


print('Случайный пароль из 7 символов:', generate_password(7))
print('10 случайных паролей длиной 15 символов:')
print(*main(10, 15), sep='\n')

