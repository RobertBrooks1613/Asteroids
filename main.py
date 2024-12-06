import pygame
import constants as CON
import os
import player as p
import asteroid as a
import asteroidfield as af

# windows env. needed so why bash calls main.py the screen shows up.
os.environ['DISPLAY'] = ':0'
os.environ['SDL_VIDEO_WINDOW_POS'] = "550,350"

# initilize player pos
x = CON.SCREEN_WIDTH / 2
y = CON.SCREEN_HEIGHT / 2

def main():
    # draw player
    player = p.Player(x,y)
    asteroids = pygame.sprite.Group()
    # initilize
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    af.AsteroidField.containers = updatable
    asteroid_field = af.AsteroidField()
    a.Asteroid.containers = (asteroids, updatable, drawable)
    
    
    updatable.add(player, asteroid_field)
    drawable.add(player)
    # screen
    screen = pygame.display.set_mode((CON.SCREEN_WIDTH, CON.SCREEN_HEIGHT))

    # random banter...
    print("Starting asteroids!")
    print(f"Screen width: {CON.SCREEN_WIDTH}")
    print(f"Screen height: {CON.SCREEN_HEIGHT}")
    
    # fps clock and delta time
    fps_clock = pygame.time.Clock()
    dt = fps_clock.tick(60) /1000
    
    # Main game loop
    while True:
        screen.fill("black")
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in updatable:
            sprite.update(dt)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        pygame.display.flip()
        fps_clock.tick(60)
    
    
    
    
if __name__ == "__main__":
    main()
