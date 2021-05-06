# БСБО-05-19 Савранский С.

import re

translatedText = None


def translate(text):
    global translatedText
    res = re.sub('[ауоыиэяюёе]', '', text, flags=re.IGNORECASE)
    translatedText = re.sub('\s+', ' ', res)


translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто читать. Достаточно небольшой '
          'тренировки - и вы сможете это делать.')
print(translatedText)
