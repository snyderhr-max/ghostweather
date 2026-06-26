import random
import py5


def draw_lightning():
    if random.random() > 0.035:
        return

    py5.stroke(230, 240, 255, 220)
    py5.stroke_weight(3)

    x = random.uniform(-60, 40)
    y = -110

    for _ in range(5):
        next_x = x + random.uniform(-35, 35)
        next_y = y + random.uniform(25, 45)
        py5.line(x, y, next_x, next_y)
        x, y = next_x, next_y

    py5.no_stroke()
