import math
import random
import py5


class ParticleSystem:
    def __init__(self, count, radius, layer=1.0, speed=1.0, alpha=1.0, size=1.0):
        self.count = count
        self.radius = radius
        self.layer = layer
        self.speed = speed
        self.alpha = alpha
        self.size = size
        self.particles = [self._make_particle() for _ in range(count)]

    def _make_particle(self):
        return {
            "angle": random.uniform(0, math.tau),
            "distance": random.uniform(5, self.radius * 0.95),
            "speed": random.uniform(0.004, 0.018),
            "size": random.uniform(2, 7),
            "brightness": random.uniform(80, 220),
            "wobble": random.uniform(0, math.tau),
            "drift": random.uniform(-0.006, 0.006),
        }

    def draw(self, t, theme):
        r, g, b = theme["particle"]
        speed_multiplier = theme["speed"] * self.speed

        for p in self.particles:
            p["angle"] += (p["speed"] * speed_multiplier) + p["drift"]

            wave = math.sin(t * 0.9 + p["wobble"]) * 13
            spiral = math.sin(p["angle"] * 3 + t * 0.6) * 7
            distance = p["distance"] + wave + spiral

            if distance > self.radius:
                p["distance"] *= 0.985
            if distance < 8:
                p["distance"] += 2

            x = math.cos(p["angle"]) * distance * self.layer
            y = math.sin(p["angle"]) * distance * 0.72 * self.layer

            depth = 0.65 + 0.35 * math.sin(p["angle"])
            size = p["size"] * depth * self.size

            edge_fade = 1 - min(abs(distance) / self.radius, 1)
            alpha = max(10, p["brightness"] * edge_fade * depth * self.alpha)

            py5.fill(r, g, b, alpha)
            py5.circle(x, y, size)
