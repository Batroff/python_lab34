# БСБО-05-19 Савранский С.

from PIL import Image
from PIL import ImageDraw


def board(num, size):
    img_size = num * size

    image = Image.new('RGB', (img_size, img_size), (255, 255, 255))
    draw = ImageDraw.Draw(image)
    
    for y in range(0, img_size, size):
        start_x = 0 if y // size % 2 == 0 else size

        for x in range(start_x, img_size, size * 2):
            draw.rectangle([x, y, x + size, y + size], fill=(0, 0, 0))

    image.save('res.png', 'PNG')


board(8, 50)

