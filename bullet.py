import pygame
import constants as con
import circleshape as cs

class Shot(cs.CircleShape):
    def __init__(self, x, y, radius: int = con.SHOT_RADIUS):
        super().__init__(x, y, radius)
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.velocity = pygame.Vector2(0, 1)
        self.rotation = 0
    
    def rotate(self, direction):
        self.rotation = direction
    def draw(self, screen):
        # sub-classes must override
        pygame.draw.circle(screen, "red", self.position, self.radius, 2)

    def update(self, dt):
        # sub-classes must override
        self.position += self.velocity * dt
    def kill(self):
        super().kill()
        self.velocity = pygame.Vector2(0, 0)