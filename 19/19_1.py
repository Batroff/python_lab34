# БСБО-05-19 Савранский С.

from calendar import different_locale, month_name


def get_month_name(month_num, locale):
    with different_locale(locale):
        return month_name[month_num]
