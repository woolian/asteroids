from circleshape import *
from constants import ASTEROID_MIN_RADIUS
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            angle = random.uniform(20,50)
            smaller_radius = self.radius - ASTEROID_MIN_RADIUS
            split1_vector = self.velocity.rotate(angle)
            split2_vector = self.velocity.rotate(-angle)
            split1_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
            split1_asteroid.velocity = split1_vector * 1.2
            split2_asteroid = Asteroid(self.position.x, self.position.y, smaller_radius)
            split2_asteroid.velocity = split2_vector * 1.2
