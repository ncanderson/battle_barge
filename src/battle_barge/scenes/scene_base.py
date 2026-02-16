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
    """

    ############################################################################

    def __init__(self,
                 scene_manager: Optional["SceneManager"] = None,
                 asset_manager: Optional["AssetManager"] = None
    ):
        """!
        @brief Constructor
        @param scene_manager Optional instance of the scene manager
        @param asset_manager Optional instance of the asset manager
        """
        self._scene_manager = scene_manager
        self._assets_manager = asset_manager

        # Optional flag for requesting a scene change
        self._next_scene = None

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
