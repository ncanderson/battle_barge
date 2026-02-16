# Standard imports
from __future__ import annotations
from typing import TYPE_CHECKING

# 3rd party imports
import pygame

# Module imports
from .scene_base import SceneBase
if TYPE_CHECKING:
    from battle_barge.managers import SceneManager
    from battle_barge.managers import AssetManager

################################################################################

class MainMenuScene(SceneBase):
    """!
    @brief Main menu scene
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

        self._title_text = "Battle Barge"

        # Set the scene manager
        self._scene_manager = scene_manager

        # Load the fonts for this scene
        self._title_font = asset_manager.get_font("kingthings-spike", 72)
        self._option_font = asset_manager.get_font("kingthings-spike", 48)

        # Menu options
        self._options = ["New Game", "Quit"]
        self._selected_index = 0

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
                if event.key == pygame.K_UP:
                    self._selected_index = (self._selected_index - 1) % len(self._options)
                elif event.key == pygame.K_DOWN:
                    self._selected_index = (self._selected_index + 1) % len(self._options)
                elif event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                    self._activate_option()

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
        screen.fill((0,0,0))  # clear

        logical_width, logical_height = screen.get_size()

        # Draw title
        title_surface = self._title_font.render(self._title_text, True, (255, 255, 255))
        title_x = logical_width // 2 - title_surface.get_width() // 2
        title_y = int(logical_height * 0.1)
        screen.blit(title_surface, (title_x, title_y))

        # Draw menu options
        start_y = logical_height * 0.3  # below title
        spacing = logical_height * 0.1

        for i, option in enumerate(self._options):
            color = (255, 255, 0) if i == self._selected_index else (255, 255, 255)
            text_surface = self._option_font.render(option, True, color)

            x = logical_width // 2 - text_surface.get_width() // 2
            y = int(start_y + i * spacing)
            screen.blit(text_surface, (x, y))

    ############################################################################
    # Private Methods

    def _activate_option(self) -> None:
        """!
        @brief Parse main menu scene options
        """
        option = self._options[self._selected_index]
        if option == "New Game":

            print("Starting new game...")

        elif option == "Quit":
            print("Quitting")
            self._scene_manager.request_quit()

################################################################################
