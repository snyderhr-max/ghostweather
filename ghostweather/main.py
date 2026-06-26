import math
import py5

from config import WIDTH, HEIGHT, FPS, PARTICLE_COUNT, DEFAULT_MODE
from themes import THEMES
from engine.particles import ParticleSystem
from engine.orb import draw_glow, draw_volumetric_core, draw_core_shell, draw_glass_shell, draw_highlight
from engine.effects import draw_lightning


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
    radius = ORB_RADIUS * pulse

    draw_glow(radius, theme)
    draw_volumetric_core(radius, theme)

    background_particles.draw(t, theme)
    mid_particles.draw(t, theme)
    foreground_particles.draw(t, theme)

    draw_core_shell(radius, theme)
    draw_glass_shell(radius)
    draw_highlight(radius)

    if MODE == "storm":
        draw_lightning()


py5.run_sketch()
