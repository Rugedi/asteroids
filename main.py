# imports
import pygame
from constants import *

#start main:
def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    black = (0, 0, 0)

    #delta time
    clock = pygame.time.Clock()
    dt  = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(black)
        pygame.display.flip()
        clock.tick(60)
        dt = clock.get_time() / 1000


    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
