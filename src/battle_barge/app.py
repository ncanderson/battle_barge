# Main entry point for the game

import pygame

def run() -> None:

    pygame.init()

    # Internal "logical" resolution for your game
    LOGICAL_SIZE = (1280, 720)

    # Create the main window: borderless + scaled
    flags = pygame.NOFRAME | pygame.SCALED
    screen = pygame.display.set_mode(LOGICAL_SIZE, flags)

    # Create a surface at the logical resolution
    surface = pygame.Surface(LOGICAL_SIZE)

    # Main loop
    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        ## Example: fill the logical surface
        #surface.fill((30, 30, 30))  # dark gray background

        # Draw something simple (centered rectangle)
        pygame.draw.rect(
            surface,
            (200, 100, 50),
            (LOGICAL_SIZE[0]//4, LOGICAL_SIZE[1]//4, LOGICAL_SIZE[0]//2, LOGICAL_SIZE[1]//2)
        )

        # Scale logical surface to actual screen
        scaled_surface = pygame.transform.scale(surface, screen.get_size())
        screen.blit(scaled_surface, (0, 0))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
