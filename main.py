import pygame
import constants as CON
import os
import player as p
import asteroid as a
import bullet as b
import asteroidfield as af
import score as s

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
    shots = pygame.sprite.Group()
    
    
    # initilize
    pygame.font.init()
    current_level_score = s.Score()
    font = pygame.font.SysFont("Comic Sans MS", 30)
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    af.AsteroidField.containers = updatable
    asteroid_field = af.AsteroidField()
    a.Asteroid.containers = (asteroids, updatable, drawable)
    b.Shot.containers = (shots, updatable, drawable)
    
    
    
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
    running = True
    while running:
        screen.fill("black")
        score_bored = font.render(f"your score: {current_level_score.get_score()}"   
                    f"  Lives: {current_level_score.get_player_life()}", 1, "white")
        screen.blit(score_bored, (CON.SCREEN_WIDTH / 2 - 125, 50))
        for sprite in drawable:
            sprite.draw(screen)
        for sprite in updatable:
            sprite.update(dt)
            if isinstance(sprite, a.Asteroid):
                if sprite.collision(player):
                    player.kill()
                    current_level_score.lose_life()
                    if current_level_score.get_player_life() > 0:
                        player = p.Player(x,y)
                        updatable.add(player)
                        drawable.add(player)
                    else:
                        running = False
                        game_over(screen)
        for sprite in updatable:
            if isinstance(sprite, b.Shot):
                for ast in asteroids:
                    if sprite.collision(ast):
                        sprite.kill()
                        ast.kill()
                        current_level_score.add_score(CON.ASTEROID_SCORE)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False   
        pygame.display.flip()
        fps_clock.tick(60)
    
    
def game_over(screen):
    game_over = True
    fps_clock = pygame.time.Clock()
    while game_over:
        screen.fill("black")
        font = pygame.font.SysFont("Comic Sans MS", 100)
        game_over = font.render("Game Over", 1, "white")
        screen.blit(game_over, (CON.SCREEN_WIDTH / 2 - 200, CON.SCREEN_HEIGHT / 2))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False    
        pygame.display.flip()
        fps_clock.tick(60)
    
if __name__ == "__main__":
    main()
