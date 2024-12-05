import pygame
import constants as CON
import os
os.environ['DISPLAY'] = ':0'
os.environ['SDL_VIDEO_WINDOW_POS'] = "550,350"

def main():
    pygame.init()
    screen = pygame.display.set_mode((CON.SCREEN_WIDTH, CON.SCREEN_HEIGHT))
    screen.fill("black")
    
    box_rect = pygame.Rect(CON.SCREEN_WIDTH,CON.SCREEN_WIDTH,CON.SCREEN_HEIGHT,CON.SCREEN_HEIGHT)
    pygame.draw.rect(screen, "black", box_rect)
    print("Starting asteroids!")
    print(f"Screen width: {CON.SCREEN_WIDTH}")
    print(f"Screen height: {CON.SCREEN_HEIGHT}")
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return    
        pygame.display.flip()
    
    
    
    
if __name__ == "__main__":
    main()
