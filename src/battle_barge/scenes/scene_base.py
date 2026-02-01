# Standard imports
from abc import ABC, abstractmethod
from importlib import resources
import pathlib

# 3rd party imports
import pygame

# Module imports

################################################################################

class SceneBase(ABC):
    """!
    @brief Abstract base class for scenes
    @details Implementing classes must implement all three of these functions
    """

    ############################################################################

    def __init__(self, app):
        """!
        @brief Constructor
        @param app The app instanace
        """
        # Boilerplate
        self._app = app
        self._next_scene = None
        self._finished = False

        # Path to assets
        pkg = sys.modules[__package__]
        self._package_root = pathlib.Path(pkg.__file__).parent
        self._assets_dir = self._package_root / "assets"

        # Fonts
        # Derived classes can set their own fonts if desired, using
        # 'self._assets_dir' to build the path to the font to load

        # A good gothicy font
        kingthings_spike = self._assets_dir / "kingthings-spike-font" / "KingthingsSpike-9X6Z.ttf"

        # Set the default font
        self._font = pygame.font.Font(kingthings_spike, 48)

    ############################################################################

    @abstractmethod
    def handle_input(self, events):
        """!
        @brief Handle event input
        @param events Pygame events
        """
        pass

    ############################################################################

    @abstractmethod
    def update(self, dt):
        """!
        @brief Handle updates
        @param dt Delta time - total elapsed time
        """
        pass

    ############################################################################

    @abstractmethod
    def draw(self, screen):
        """!
        @brief Re-draw the scene
        @param screen Game screen to draw to
        """
        pass

################################################################################
