import math
import random
import py5

from config import WIDTH, HEIGHT, FPS, PARTICLE_COUNT, DEFAULT_MODE
from themes import THEMES
from engine.particles import ParticleSystem


MODE = DEFAULT_MODE
ORB_RADIUS = 120

background_particles = None
mid_particles = None
foreground_particles = None


def setup():
    global background_particles, mid_particles, foreground_particles

    py5.size(WIDTH, HEIGHT)
    py5.frame_rate(FPS)
    py5.no_stroke()

    background_particles = ParticleSystem(90, ORB_RADIUS, layer=0.78, speed=0.45, alpha=0.35, size=1.7)
    mid_particles = ParticleSystem(120, ORB_RADIUS, layer=1.0, speed=1.0, alpha=0.75, size=1.0)
    foreground_particles = ParticleSystem(45, ORB_RADIUS, layer=1.12, speed=1.35, alpha=1.0, size=0.75)


def draw():
    theme = THEMES.get(MODE, THEMES["rain"])

    py5.background(0)
    py5.translate(WIDTH / 2, HEIGHT / 2)

    t = py5.frame_count * 0.05
    pulse = 1 + 0.04 * math.sin(t)

    draw_glow(ORB_RADIUS * pulse, theme)
    background_particles.draw(t, theme)
    mid_particles.draw(t, theme)
    foreground_particles.draw(t, theme)
    draw_core_shell(ORB_RADIUS * pulse, theme)
    draw_glass_shell(ORB_RADIUS * pulse)
    draw_highlight(ORB_RADIUS * pulse)

    if MODE == "storm":
        draw_lightning()


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


py5.run_sketch()
