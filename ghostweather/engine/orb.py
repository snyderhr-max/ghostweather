import math
import py5


def draw_glow(radius, theme):
    r, g, b = theme["glow"]

    for i in range(20, 0, -1):
        alpha = 4 + i * 2
        py5.fill(r, g, b, alpha)
        py5.circle(0, 0, radius + i * 14)


def draw_core_shell(radius, theme):
    r, g, b = theme["core"]

    py5.fill(r, g, b, 55)
    py5.circle(0, 0, radius * 2)

    py5.fill(255, 255, 255, 28)
    py5.circle(0, 0, radius * 1.5)


def draw_glass_shell(radius):
    py5.no_fill()

    py5.stroke(255, 255, 255, 22)
    py5.stroke_weight(2.2)
    py5.circle(0, 0, radius * 2.03)

    py5.stroke(180, 220, 255, 10)
    py5.stroke_weight(5)
    py5.circle(0, 0, radius * 1.97)

    py5.stroke(255, 255, 255, 14)
    py5.stroke_weight(3)
    py5.arc(0, 0, radius * 1.9, radius * 1.9, math.radians(30), math.radians(150))

    py5.no_stroke()


def draw_highlight(radius):
    py5.fill(255, 255, 255, 70)
    py5.circle(-radius * 0.35, -radius * 0.42, radius * 0.42)
