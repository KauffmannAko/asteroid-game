import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField  # Import the AsteroidField class

def main():
    pygame.init()

    # Set up the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    pygame.time.Clock()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    asteroid_field = AsteroidField()  # Create an instance of AsteroidField
    dt = 0

    # Set the screen title
    pygame.display.set_caption("Asteroids V.0.1")

    # Create groups for updatable and drawable objects
    updatable = [player, asteroid_field]
    drawable = [player]

    while True:
        # Check for quit event
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # Update all objects in the updatable group
        for obj in updatable:
            obj.update(dt)

        # Clear the screen
        screen.fill("black")

        # Draw all objects in the drawable group
        for obj in drawable:
            obj.draw(screen)

        # Update the display
        pygame.display.flip()

        # Limit the frame rate to 60 FPS and calculate delta time
        clock = pygame.time.Clock()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()