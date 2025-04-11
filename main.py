import sys
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
from shot import *


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable
    Shot.containers = (shots, updatable, drawable)

    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    asteroid_field = AsteroidField()

    clock = pygame.time.Clock()
    dt = 0

    # game loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black")
        # player.draw(screen)
        for obj in drawable:
            obj.draw(screen)
        # player.update(dt)
        updatable.update(dt)
        for ast in asteroids:
            if ast.is_collision(player):
                print("Game over!")
                sys.exit()

            for shot in shots:
                if shot.is_collision(ast):
                    shot.kill()
                    ast.split()
                    
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()