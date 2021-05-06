# БСБО-05-19 Савранский С.

def bracket_check(test_string):
    if test_string.count('(') != test_string.count(')'):
        print('NO')
        return

    while len(test_string) > 0:
        if (first := test_string.index('(')) < (last := test_string.index(')')):
            test_string = test_string[:first] + test_string[first+1:last] + test_string[last+1:]
        else:
            print('NO')
            return

    print('YES')
