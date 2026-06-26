import math
import random
import py5

WIDTH = 720
HEIGHT = 720
PARTICLE_COUNT = 220

MODE = "storm"  # clear, clouds, rain, storm, snow

particles = []


THEMES = {
    "clear": {
        "glow": (255, 175, 45),
        "core": (255, 190, 70),
        "particle": (255, 230, 120),
        "speed": 0.75,
    },
    "clouds": {
        "glow": (160, 175, 200),
        "core": (180, 190, 210),
        "particle": (235, 240, 255),
        "speed": 0.45,
    },
    "rain": {
        "glow": (40, 140, 255),
        "core": (40, 130, 255),
        "particle": (130, 210, 255),
        "speed": 1.0,
    },
    "storm": {
        "glow": (80, 90, 190),
        "core": (45, 55, 150),
        "particle": (180, 210, 255),
        "speed": 1.55,
    },
    "snow": {
        "glow": (170, 230, 255),
        "core": (150, 220, 255),
        "particle": (245, 255, 255),
        "speed": 0.35,
    },
}


def setup():
    py5.size(WIDTH, HEIGHT)
    py5.frame_rate(30)
    py5.no_stroke()

    for _ in range(PARTICLE_COUNT):
        particles.append(make_particle())


def make_particle():
    angle = random.uniform(0, math.tau)
    distance = random.uniform(0, 115)

    return {
        "angle": angle,
        "distance": distance,
        "speed": random.uniform(0.006, 0.022),
        "size": random.uniform(2, 7),
        "brightness": random.uniform(80, 210),
        "wobble": random.uniform(0, math.tau),
    }


def draw():
    theme = THEMES.get(MODE, THEMES["rain"])

    py5.background(0)
    py5.translate(WIDTH / 2, HEIGHT / 2)

    t = py5.frame_count * 0.05
    pulse = 1 + 0.04 * math.sin(t)

    draw_glow(120 * pulse, theme)
    draw_particles(t, 120, theme)
    draw_core_shell(120 * pulse, theme)
    draw_highlight(120 * pulse)

    if MODE == "storm":
        draw_lightning()


def draw_glow(radius, theme):
    r, g, b = theme["glow"]

    for i in range(20, 0, -1):
        alpha = 4 + i * 2
        py5.fill(r, g, b, alpha)
        py5.circle(0, 0, radius + i * 14)


def draw_particles(t, orb_radius, theme):
    r, g, b = theme["particle"]
    speed_multiplier = theme["speed"]

    for p in particles:
        p["angle"] += p["speed"] * speed_multiplier

        wobble = math.sin(t + p["wobble"]) * 10
        distance = p["distance"] + wobble

        x = math.cos(p["angle"]) * distance
        y = math.sin(p["angle"]) * distance * 0.72

        edge_fade = 1 - min(distance / orb_radius, 1)
        alpha = max(20, p["brightness"] * edge_fade)

        py5.fill(r, g, b, alpha)
        py5.circle(x, y, p["size"])


def draw_core_shell(radius, theme):
    r, g, b = theme["core"]

    py5.fill(r, g, b, 55)
    py5.circle(0, 0, radius * 2)

    py5.fill(255, 255, 255, 28)
    py5.circle(0, 0, radius * 1.5)


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