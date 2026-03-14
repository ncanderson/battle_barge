# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports
from .scene_base import SceneBase

################################################################################

class PlanetSelectionScene(SceneBase):
    """!
    @brief New game scene
    """

    ############################################################################

    def __init__(self,
                 scene_manager: SceneManager,
                 asset_manager: AssetManager,
                 game_state: GameState):
        """!
        @brief Constructor
        @param assets Instance of the AssetManager
        """
        super().__init__(scene_manager, asset_manager, game_state)

        # Set the necessary manager attributes
        self._scene_manager = scene_manager
        self._asset_manager = asset_manager
        self._game_state = game_state

    ############################################################################
    # Lifecycle hooks

    def on_enter(self):
        """!
        @brief Called when the scene becomes active (pushed or changed)
        """
        pass

    ############################################################################

    def on_exit(self):
        """!
        @brief Called when the scene is removed from the stack
        """
        pass

    ############################################################################
    # Public Methods

    def handle_input(self, events):
        """!
        @brief Handle event input
        @param events Pygame events
        """
        for event in events:
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
        screen.fill((0, 0, 0))

        text = self._text_font.render(f"Planet Selection, difficulty: {self._game_state.difficulty}",
                                      True,
                                      (255, 255, 255))

        x = screen.get_width() // 2 - text.get_width() // 2
        y = screen.get_height() // 2 - text.get_height() // 2

        screen.blit(text, (x, y))

    ############################################################################
    # Private Methods

################################################################################
