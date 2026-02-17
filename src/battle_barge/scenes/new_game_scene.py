# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports
from .scene_base import SceneBase

################################################################################

class NewGameScene(SceneBase):
    """!
    @brief New game scene
    """

    ############################################################################

    def __init__(self,
                 scene_manager: SceneManager,
                 asset_manager: AssetManager):
        """!
        @brief Constructor
        @param assets Instance of the AssetManager
        """
        super().__init__()

        # Set the necessary manager attributes
        self._scene_manager = scene_manager
        self._asset_manager = asset_manager

        # placeholder
        self._text_font = asset_manager.get_font("kingthings-spike", 48)

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
            if event.type == pygame.KEYDOWN:
                # Exit this scene with spacebar
                if event.key == pygame.K_SPACE:
                    self._scene_manager.pop()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect and self.button_rect.collidepoint(event.pos):
                    self._scene_manager.pop()

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
        new_game_text = ""

        screen.fill((0, 0, 0))

        # Draw text centered
        logical_width, logical_height = screen.get_size()

        text_surface = self._text_font.render(new_game_text, True, (255, 255, 255))

        x = logical_width // 2 - text_surface.get_width() // 2
        y = logical_height // 2 - text_surface.get_height() // 2
        screen.blit(text_surface, (x, y))

        # Draw a prompt below the text
        prompt_surface = self._text_font.render("Press Space or Click to continue", True, (255, 255, 0))
        prompt_x = logical_width // 2 - prompt_surface.get_width() // 2
        prompt_y = y + text_surface.get_height() + 20
        screen.blit(prompt_surface, (prompt_x, prompt_y))

        # Store prompt rectangle for click detection
        self.button_rect = pygame.Rect(prompt_x,
                                       prompt_y,
                                       prompt_surface.get_width(),
                                       prompt_surface.get_height())

    ############################################################################
    # Private Methods

################################################################################
