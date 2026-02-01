# Main entry point for the game

# Standard imports
import pygame

# 3rd party imports

# Module imports
from .scenes import MainMenuScene
from .managers import InputManager

################################################################################

class App:
    """!
    @brief Main class, managing all game state
    """

    ############################################################################

    def __init__(self, scene):
        """!
        @brief Set up main game object
        @param scene Starting game scene
        """
        # Internal "logical" resolution
        self._LOGICAL_SIZE = (1280, 720)

        # Create a surface at the logical resolution
        self._surface = pygame.Surface(self._LOGICAL_SIZE)
        self._screen = self._initialize_game_window()

        # Runtime helpers
        self._clock = pygame.time.Clock()
        self._running = False

        # Start with the main menu scene
        self._scene = scene

        # Define the path to the assets directory, so anything with access to App
        # can load resources
        root_dir = Path(__file__).parent
        self._assets_dir = root_dir / "assets"

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

        # Maybe these should be class attrs?
        input_mngr = InputManager()

        #################################
        # Main loop

        while self._running:

            # Get events
            events = pygame.event.get()

            # Check for a quit event
            for event in events:
                if event.type == pygame.QUIT:
                    self._quit()

            # Check for user inputs
            input_mngr.update(events)

            # Scale logical surface to actual screen
            scaled_surface = pygame.transform.scale(self._surface,
                                                    self._screen.get_size())
            self._screen.blit(scaled_surface, (0, 0))

            pygame.display.flip()
            self._clock.tick(60)

    ############################################################################

    def get_assets_dir(self) -> str:
        """!
        @brief Get the path to the assets directory
        @return The absolute path to the assets directory
        """
        return self._assets_dir

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
        app = cls(MainMenuScene(None))
        # Re-inject app into the new scene, so the scene can access app
        app._scene.app = app

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

    def _quit(self) -> None:
        """!
        @brief Quit the game
        """
        self._running = False

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
