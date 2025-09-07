# imports
import sys
import pygame
from constants import *
from player import *
from circleshape import *
from asteroid import *
from asteroidfield import *
from shot import *

#start main:
def main():
    pygame.init()
    start_ticks = pygame.time.get_ticks()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    black = (0, 0, 0)
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2, PLAYER_RADIUS)
    asteroidfield = AsteroidField()
    #delta time
    clock = pygame.time.Clock()
    dt = 0


    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen.fill(black)
        for object in drawable:
            object.draw(screen)
        
        updatable.update(dt)
        for meteor in asteroids:
            if meteor.collides_with(player):
                print("Game over!")
                sys.exit()

        for meteor in asteroids:
            for shot in shots:
                if meteor.collides_with(shot):
                    meteor.split()
                    shot.kill()

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        


    #print("Starting Asteroids!")
    #print(f"Screen width: {SCREEN_WIDTH}")
    #print(f"Screen height: {SCREEN_HEIGHT}")


if __name__ == "__main__":
    main()
