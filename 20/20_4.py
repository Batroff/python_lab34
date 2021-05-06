# БСБО-05-19 Савранский С.

def hello(name):
    print(f'Здравствуйте, {name}! Вашу карту ищут...')


def search_card(name):
    global base
    print(f'Ваша карта с номером {base.index(name) + 1} найдена' if name in base else 'Ваша карта не найдена')
