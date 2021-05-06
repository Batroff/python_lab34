# БСБО-05-19 Савранский С.

horses = {1: False, 2: False, 3: False, 4: False, 5: False, 6: False, 7: False, 8: False, 9: False, 10: False}


def do_bet(num, bet):
    global horses

    if 1 <= num <= 10 and bet > 0:
        if horses.get(num) is False:
            horses[num] = True
            print(f'Ваша ставка в размере {bet} на лошадь {num} принята')
            return
    print('Что-то пошло не так, попробуйте еще раз')
