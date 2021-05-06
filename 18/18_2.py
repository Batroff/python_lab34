# БСБО-05-19 Савранский С.

def ask_password():
    password = '123'

    for _ in range(3):
        if password == input('Password >> '):
            print('Пароль принят')
            return
    print('В доступе отказано')
