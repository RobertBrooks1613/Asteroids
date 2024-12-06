import circleshape as cs
import constants as con
import pygame
class Player(cs.CircleShape):
    
    def __init__(self, initial_x: int = 0, initial_y: int = 0,radius: int = con.PLAYER_RADIUS):
        super().__init__(initial_x, initial_y, radius)
        self.rotation = 0
    
        # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        pygame.draw.polygon(surface=screen,color="white", points=self.triangle(), width=2)
        
    def rotate(self, dt):
        self.rotation += con.PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * con.PLAYER_SPEED * dt
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(dt)
        if keys[pygame.K_d]:
            self.rotate(-dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        