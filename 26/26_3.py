# БСБО-05-19 Савранский С.

from PIL import Image


def makeanagliph(filename, delta):
    src = Image.open(filename, 'r')
    x, y = src.size
    pixels_src = src.load()

    res = Image.new('RGB', (x, y), (0, 0, 0))
    pixels_res = res.load()

    for i in range(x):
        for j in range(y):
            if i < delta:
                r, g, b = pixels_src[i, j]
                pixels_res[i, j] = 0, g, b
            else:
                pixels_res[i, j] = r, g, b
                g, b = pixels_src[i, j][1:]
                r = pixels_src[i - delta, j][0]

    res.save('res.png', 'PNG')


makeanagliph('source.jpeg', 10)

