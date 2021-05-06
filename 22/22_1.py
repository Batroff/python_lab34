# БСБО-05-19 Савранский С.

alp = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def encrypt_caesar(msg, shift):
    res = ''
    for ch in msg:
        rep_ch = ch if (i := alp.find(ch.lower())) == -1 else alp[(i + shift) % len(alp)]
        res += rep_ch.upper() if ch.isupper() else rep_ch
    return res


def decrypt_caesar(msg, shift):
    res = ''
    for ch in msg:
        rep_ch = ch if (i := alp.find(ch.lower())) == -1 else alp[(len(alp) + i - shift) % len(alp)]
        res += rep_ch.upper() if ch.isupper() else rep_ch
    return res

