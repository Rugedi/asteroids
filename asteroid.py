import pygame
from constants import *
from circleshape import CircleShape
import random

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, width = 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
        	return
        rotate_angle = random.uniform(20, 50)
        new_angle_1 = pygame.Vector2.rotate(self.velocity, rotate_angle)
        new_angle_2 = pygame.Vector2.rotate(self.velocity, -rotate_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        Asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
        Asteroid1.velocity = new_angle_1 * 1.2   # 1.2 increases speed
        Asteroid2.velocity = new_angle_2 * 1.2