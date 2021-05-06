# БСБО-05-19 Савранский С.

person_name = None
person_vacationDates = None


def setup_profile(name, vacationDates):
    global person_name
    global person_vacationDates

    person_name = name
    person_vacationDates = vacationDates


def print_application_for_leave():
    print(f'Заявление на отпуск в период {person_vacationDates}. {person_name}')


def print_holiday_money_claim(amount):
    print(f'Прошу выплатить {amount} отпускных денег. {person_name}')


def print_attorney_letter(toWhom):
    print(f'На время отпуска в период {person_vacationDates} моим заместителем назначается {toWhom}. {person_name}')
