# Main entry point for the game

# Standard imports
import pygame
from pathlib import Path

# 3rd party imports

# Module imports
from .managers import AssetManager
from .managers import InputManager
from .scenes import MainMenuScene

################################################################################

class App:
    """!
    @brief Main class, managing all game state
    """

    ############################################################################

    def __init__(self):
        """!
        @brief Set up main game object
        """
        # Internal "logical" resolution
        self._LOGICAL_SIZE = (1280, 720)

        # Create a surface at the logical resolution
        self._surface = pygame.Surface(self._LOGICAL_SIZE)
        self._screen = self._initialize_game_window()

        # Runtime helpers
        self._clock = pygame.time.Clock()
        self._running = False

        # Define the path to the assets directory, so anything with access to App
        # can load resources
        root_dir = Path(__file__).parent
        self._assets = AssetManager(root_dir)

        # Create the Input Manager
        self._input_mngr = InputManager()

    ############################################################################
    # Public Methods

    def run(self) -> None:
        """!
        @brief Main run loop of the game
        @details This function is responsible for managing the lifetime of all
        game objects and the main game loop
        """

        #################################
        # Runtime object initialization

        self._running = True

        #################################
        # Main loop

        while self._running:

            # Delta time in seconds, 60 FPS cap
            dt = self._clock.tick(60) / 1000

            # Get events
            events = pygame.event.get()

            # Check for a quit event
            for event in events:
                if event.type == pygame.QUIT:
                    self.quit()

            # Handle input in the current scene
            if self._scene:
                self._scene.handle_input(events)

            # Update current scene
            if self._scene:
                self._scene.update(dt)

            # Clear logical surface
            self._surface.fill((0, 0, 0))

            # Draw scene to logical surface
            if self._scene:
                self._scene.draw(self._surface)

            ## Check for user inputs
            # Is this needed anymore?
            #self._input_mngr.update(events)

            # Scale logical surface to actual screen
            scaled_surface = pygame.transform.scale(self._surface,
                                                    self._screen.get_size())
            self._screen.blit(scaled_surface, (0, 0))

            pygame.display.flip()

    ############################################################################

    def set_start_scene(self, scene) -> None:
        """!
        @brief Initialize the game's first scene
        @param scene Starting game scene
        """
        self._scene = scene

    ############################################################################

    def assets(self) -> str:
        """!
        @brief Get the asset manager
        @return The asset manager
        """
        return self._assets

    ############################################################################

    def quit(self) -> None:
        """!
        @brief Quit the game
        """
        self._running = False

    ############################################################################
    # Class Methods

    @classmethod
    def Init_app(cls):
        """!
        @brief Initialization, providing a class method for external callers
        to set up the game
        """
        pygame.init()

        # Initialize the app, starting with the MainMenuScene
        app = cls()
        # Re-inject app into the new scene, so the scene can access app
        app.set_start_scene(MainMenuScene(app))

        # Run
        app.run()

        # Exit
        pygame.quit()

    ############################################################################
    # Private Methods

    def _change_scene(self, scene) -> None:
        """!
        @brief Change the game scene
        @param scene The new scene to set as the active scene
        """
        self._scene = scene

    ############################################################################

    def _initialize_game_window(self) -> pygame.Surface:
        """!
        @breif Set up the main game window
        """
        # Config for the main game window
        flags = pygame.NOFRAME | pygame.SCALED | pygame.FULLSCREEN

        # Return the configurd screen
        return pygame.display.set_mode(self._LOGICAL_SIZE, flags)

################################################################################
