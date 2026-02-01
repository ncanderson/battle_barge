# Standard imports
import pygame

# 3rd party imports

# Module imports
from .scene_base import SceneBase

################################################################################

class MainMenuScene(SceneBase):
    """!
    @brief Main menu scene
    """

    ############################################################################

    def __init__(self, app):
        """!
        @brief Constructor
        @param app Reference to main game app
        """
        super().__init__(app)

    ############################################################################

    def handle_input(self, events):
        """!
        @brief Handle event input
        @param events Pygame events
        """
        pass

    ############################################################################

    def update(self, dt):
        """!
        @brief Handle updates
        @param dt Delta time - total elapsed time
        """
        pass

    ############################################################################

    def draw(self, screen):
        """!
        @brief Re-draw the scene
        @param screen Game screen to draw to
        """
        pass

################################################################################
