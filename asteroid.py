import random

from circleshape import *
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def split(self):
        self.kill()

        # is smallest asteroid then don't split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        
        # otherwise split into two smaller asteroids
        # randomize new trajectories of smaller asteroids
        random_angle = random.uniform(20, 50)
        vector_1 = pygame.Vector2.rotate(self.velocity, random_angle)
        vector_2 = pygame.Vector2.rotate(self.velocity, -random_angle)

        new_radius = self.radius - ASTEROID_MIN_RADIUS

        new_asteroid_1 = Asteroid(self.position.x, self.position.y, new_radius)
        new_asteroid_2 = Asteroid(self.position.x, self.position.y, new_radius)

        new_asteroid_1.velocity = vector_1 * 1.2
        new_asteroid_2.velocity = vector_2 * 1.2


    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)

    def update(self, dt):
        self.position += (self.velocity * dt)