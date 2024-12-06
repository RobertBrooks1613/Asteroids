import circleshape as cs
import bullet as b
import constants as con
import pygame
class Player(cs.CircleShape):
    
    def __init__(self, initial_x: int = 0, initial_y: int = 0,radius: int = con.PLAYER_RADIUS):
        super().__init__(initial_x, initial_y, radius)
        self.rotation = 0
        self.shoot_timer = 0
    
        # in the player class
    def triangle(self):
        """
        Calculate the points of the triangle representing the player ship.

        Returns:
            list of 3 pygame.Vector2
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    def draw(self, screen):
        """
        Draw the player ship.
        Parameters:
            screen (pygame.Surface): surface to draw on
        """
        pygame.draw.polygon(surface=screen,color="white", points=self.triangle(), width=2)
        
    def rotate(self, dt):
        """
        Rotate the player ship to the left or right.
        Parameters
        ----------
        dt : float
            The time elapsed since the last frame, in seconds.
        Returns
        -------
        None
        """
        self.rotation += con.PLAYER_TURN_SPEED * dt
    
    def move(self, dt):
        """
        Move the player in the direction it is facing.
        Parameters
        ----------
        dt : float
            The time elapsed since the last frame, in seconds.
        Returns
        -------
        None
        """
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * con.PLAYER_SPEED * dt
    
    def shoot(self):
        """
        Create a new shot at the position of the player, 
        facing the direction the player is facing.
        Returns:
            b.Shot: The new shot.
        """
        new_shot = b.Shot(self.position.x, self.position.y)
        shot_velocity = pygame.Vector2(0, 1)
        shot_velocity = shot_velocity.rotate(self.rotation)
        shot_velocity *= con.PLAYER_SHOOT_SPEED
        new_shot.velocity = shot_velocity

        return new_shot
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE] and self.shoot_timer <= 0:
            self.shoot()
            self.shoot_timer = con.PLAYER_SHOOT_CD

        if self.shoot_timer > 0:
            self.shoot_timer -= dt