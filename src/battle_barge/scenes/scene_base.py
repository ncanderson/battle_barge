# Standard imports
from abc import ABC, abstractmethod
from importlib import resources
from typing import Optional
import pathlib
import sys

# 3rd party imports
import pygame

# Module imports
from battle_barge.managers import AssetManager

################################################################################

class SceneBase(ABC):
    """!
    @brief Abstract base class for scenes
    @details Implementing classes must implement all three of these functions
    """

    ############################################################################

    def __init__(self, assets: Optional[AssetManager] = None):
        """!
        @brief Constructor
        @param assets Optional instance of the asset manager
        """
        # Manager is injected when scene is added to the stack
        self._manager = None

        # Optional flag for requesting a scene change
        self._next_scene = None

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
