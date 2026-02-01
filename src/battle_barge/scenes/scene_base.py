# Standard imports
from abc import ABC, abstractmethod

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
        self._app = app
        self._next_scene = None
        self._finished = False

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
