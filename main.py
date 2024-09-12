import pygame
from constants import * 

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    game_loop(screen)

def game_loop(screen):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((10, 10, 10))
        pygame.display.flip()

if __name__ == "__main__":
    main()
