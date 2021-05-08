# БСБО-05-19 Савранский С.

from PIL import Image


def image_filter(pixels, i, j):
    return tuple(map(lambda x: x // 10, pixels[i, j]))


image = Image.open('image.jpeg', 'r')
x, y = image.size
pixels = image.load()

res = Image.new('RGB', (x, y), (0, 0, 0))
res_pixels = res.load()
for i in range(x):
    for j in range(y):
        res_pixels[i, j] = image_filter(pixels, i, j)

res.save('res.png', 'PNG')
