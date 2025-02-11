import pygame # type: ignore
from constants import *
from player import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0 
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill((0,0,0)) # black - RGB value
        player.update(dt)
        player.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60)/1000 # limits framerate to 60 FPS

if __name__ == "__main__":
    main()
