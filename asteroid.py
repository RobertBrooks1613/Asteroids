import circleshape as cs
import constants as con
import pygame
import random as rd
import score

class Asteroid(cs.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)

    
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "white", self.position, self.radius, 2)
    
    def update(self, dt):
        self.position += self.velocity * dt
    
    def kill(self):
        super().kill()
        if self.split() != "small asteroid":
            return "split!"
        else:
            self.velocity = pygame.Vector2(0, 0)
        
    def split(self):
        """
        Split this asteroid into two smaller asteroids.
        If the asteroid is too small, just return 'small asteroid'
        Returns:
            tuple of two Asteroid objects
        """
        if self.radius > con.ASTEROID_MIN_RADIUS:
            new_asteroid = Asteroid(self.position.x, self.position.y, self.radius - con.ASTEROID_MIN_RADIUS)
            new_asteroid.velocity = self.velocity.rotate(rd.uniform(20, 50))
            new_asteroid.velocity *= 1.2
            new_asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - con.ASTEROID_MIN_RADIUS)
            new_asteroid2.velocity = self.velocity.rotate(rd.uniform(-50, -20))
            new_asteroid2.velocity *= 1.2
            return new_asteroid, new_asteroid2
        else:
            return "small asteroid"