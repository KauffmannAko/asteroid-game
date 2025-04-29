import pygame
from constants import *

def main():
    pygame.init()

    # Set up the screen dimensions
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Set the screen title
    pygame.display.set_caption("Asteroids V.0.1")
    
    while True:
        # Check for quit event
        # This is a loop that will run until the user closes the window

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                print(event.type)
                pygame.quit()
                return

        screen.fill("BLACK")  # Fill the screen with black color
        pygame.display.flip() #
    
if __name__ == "__main__":
    main()