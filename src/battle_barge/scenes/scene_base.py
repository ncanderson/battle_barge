# Standard imports
from abc import ABC, abstractmethod
from importlib import resources
from typing import Optional
import pathlib
import sys

# 3rd party imports
import pygame

# Module imports

################################################################################

class SceneBase(ABC):
    """!
    @brief Abstract base class for scenes
    @details Implementing classes must implement all three of these functions
    If desired, this is a good placeholder for new scenes, to make sure you are
    transitioning into them successfully:

    screen.fill((0, 0, 0))

    text = self._text_font.render("SceneName",
                                  True,
                                  (255, 255, 255))

    x = screen.get_width() // 2 - text.get_width() // 2
    y = screen.get_height() // 2 - text.get_height() // 2

    screen.blit(text, (x, y))
    """

    ############################################################################

    def __init__(self,
                 app: Optional["App"] = None
    ):
        """!
        @brief Constructor
        @param app
        """
        self._app = app

        # Optional flag for requesting a scene change
        self._next_scene = None

        # Empty vector to use in conjunction with the drawing tools
        self._polygon_points = []

        # Load fonts for derived classes
        self._title_font = app.asset_manager.get_font("metal-lord", 72)
        self._menu_option_font = app.asset_manager.get_font("metal-lord", 48)
        self._text_font = app.asset_manager.get_font("metal-lord", 24)

    ############################################################################
    # Class properties

    @property
    def next_scene(self):
        return self._next_scene

    ############################################################################
    # Lifecycle hooks

    @abstractmethod
    def on_enter(self):
        """!
        @brief Called when the scene becomes active (pushed or changed)
        """
        pass

    ############################################################################

    @abstractmethod
    def on_exit(self):
        """!
        @brief Called when the scene is removed from the stack
        """
        pass

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
    def draw(self, surface):
        """!
        @brief Re-draw the scene
        @param screen Game screen to draw to
        """
        pass

################################################################################
