# Main entry point for the game

# Standard imports
import pygame

# 3rd party imports

# Module imports
from .managers import InputManager

def run() -> None:

    pygame.init()

    #################################
    # Screen Initialization

    # Internal "logical" resolution for your game
    LOGICAL_SIZE = (1280, 720)

    # Create the main window: borderless + scaled
    flags = pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN
    screen = pygame.display.set_mode(LOGICAL_SIZE, flags)

    # Create a surface at the logical resolution
    surface = pygame.Surface(LOGICAL_SIZE)

    #################################
    # Runtime object initialization

    input_mngr = InputManager()


    #################################
    # Main loop

    running = True
    clock = pygame.time.Clock()

    while running:

        # Get events
        events = pygame.event.get()

        # Check for a quit event
        for event in events:
            if event.type == pygame.QUIT:
                running = False

        # Check for user inputs
        input_mngr.update(events)



        # Scale logical surface to actual screen
        scaled_surface = pygame.transform.scale(surface, screen.get_size())
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
