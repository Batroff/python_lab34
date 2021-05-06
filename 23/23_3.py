# БСБО-05-19 Савранский С.

import re

phrases = input('Line >> ').split(' ')
phrases_len = list(
        map(lambda phrase: len(re.findall(
                re.compile('[ауоыиэяюёе]', re.IGNORECASE), phrase)
            ), phrases)
        )

print('Парам пам-пам' if all([False for i in phrases_len if i != phrases_len[0]]) else 'Пам парам')

