# БСБО-05-19 Савранский С.

from PIL import Image
from PIL import ImageDraw

image = Image.new('RGB', (800, 400), (230, 230, 230))
font_color = (0, 0, 0)

draw = ImageDraw.Draw(image)
draw.line([(150, 100), (100, 50), (50, 100), (115, 165), (65, 215), (15, 165)], width=3, fill=font_color)
draw.line([(300, 50), (200, 50), (200, 215), (300, 215)], width=3, fill=font_color)
draw.line([(200, 132.5), (300, 132.5)], width=3, fill=font_color)
draw.ellipse([350, 50, 450, 150], width=3, outline=font_color)
draw.line([(350, 50), (350, 215)], width=3, fill=font_color)
draw.line([(350, 132.5), (450, 215)], width=3, fill=font_color)
draw.line([(600, 50), (500, 50), (500, 215), (600, 215), (600, 132.5), (575, 132.5)], width=3, fill=font_color)

image.save('name.png', 'PNG')

