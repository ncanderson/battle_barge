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
        # Load the font for this scene
        self._font = app.assets().get_font("kingthings-spike", 48)

        # Menu options
        self._options = ["New Game", "Quit"]
        self._selected_index = 0

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
        # Black background
        screen.fill((0, 0, 0))

        for i, option in enumerate(self._options):
            # Highlight the currently selected option
            color = (255, 255, 0) if i == self._selected_index else (255, 255, 255)
            text_surface = self._font.render(option, True, color)

            # Center horizontally
            x = screen.get_width() // 2 - text_surface.get_width() // 2
            # Stack vertically with spacing
            y = 200 + i * 80
            screen.blit(text_surface, (x, y))

    ############################################################################
    # Private Methods

    def _activate_option(self) -> None:
        """!
        @brief Parse main menu scene options
        """
        option = self._options[self._selected_index]
        if option == "New Game":
            # switch to your actual game scene
            print("Starting new game...")
            # Example: self.app.scene = GameScene(self.app)
        elif option == "Quit":
            self._app.quit()

################################################################################
