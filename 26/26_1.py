# БСБО-05-19 Савранский С.

from PIL import Image
from PIL import ImageDraw

def gradient(color):
    width = 512
    height = 200
    image = Image.new('RGB', (width, height), (255, 255, 255))
    
    draw = ImageDraw.Draw(image)

    clr = (0, 0, 0)
    def _inc_color(c):
        return {'R': (c[0] + 1, *c[1:]),
                'G': (c[0], c[1] + 1, c[2]),
                'B': (*c[0:2], c[2] + 1)
                }.get(color.upper())

    for i in range(0, width, 2):
        draw.rectangle([i, 0, i + 1, height], fill=clr)
        clr = _inc_color(clr)

    image.save('res.png', 'PNG')


gradient('B')
