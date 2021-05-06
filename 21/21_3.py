# БСБО-05-19 Савранский С.

def swap(f, s):
    tmp = f[:]
    for i in range(len(f)):
        f.pop()
    f.extend(s)
    for i in range(len(s)):
        s.pop()
    s.extend(tmp)


first = [1, 2, 3]
second = [4, 5, 6]
first_content = first[:]
second_content = second[:]
swap(first, second)
print(first, second_content, first == second_content)
print(second, first_content, second == first_content)