import pygame # type: ignore
import sys
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    updatable = pygame.sprite.Group() # group of updatable objects
    drawable = pygame.sprite.Group() # group of drawable objects 
    asteroids = pygame.sprite.Group() # group of asteroid objects
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable,)
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) # black - RGB value
        updatable.update(dt)
        for asters in asteroids:
            if asters.check_collision(player) == True:
                sys.exit("Game over!")
        for each in drawable:
            each.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000 # limits framerate to 60 FPS

if __name__ == "__main__":
    main()
