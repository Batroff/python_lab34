# БСБО-05-19 Савранский С.

from PIL import Image


def make_preview(size, n_colors):
    src = Image.open('image.jpeg', 'r')

    res = src.resize(size)
    res = res.quantize(n_colors)
    res.save('res.png', 'PNG')


make_preview((120, 250), 25)
