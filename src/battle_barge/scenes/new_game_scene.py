# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports
from .scene_base import SceneBase
from .galaxy_difficulty_scene import GalaxyDifficultyScene

################################################################################

class NewGameScene(SceneBase):
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
            if event.type == pygame.KEYDOWN:
                # Exit this scene with spacebar
                if event.key == pygame.K_SPACE:
                    self._scene_manager.change_scene(GalaxyDifficultyScene(self._scene_manager,
                                                                           self._asset_manager,
                                                                           self._game_state))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect and self.button_rect.collidepoint(event.pos):
                    self._scene_manager.change_scene(GalaxyDifficultyScene(self._scene_manager,
                                                                           self._asset_manager,
                                                                           self._game_state))

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
        new_game_text = r"""
        The galaxy burns.
        Across a million stars, the banners of the Empire struggle to hold back the darkness.
        Rebellions fester in forgotten systems. Alien warbands prowl the void between trade routes.
        Entire sectors fall silent, their distress calls swallowed by the cold of space.
        To stand against this chaos, the Empire forged its greatest instruments of war:
        the Battle Barges. Vast cathedral-ships of steel and fury, they carry the Empire's
        judgment from one star system to the next. Wherever they arrive, war follows.
        You are newly appointed commander of one such vessel.
        """

        screen.fill((0, 0, 0))

        # Draw text centered
        logical_width, logical_height = screen.get_size()

        text_rect = pygame.Rect(
            logical_width * 0.15,
            logical_height * 0.15,
            logical_width * 0.7,
            logical_height * 0.6
        )

        self._draw_wrapped_text(
            screen,
            new_game_text,
            self._text_font,
            (255, 255, 255),
            text_rect
        )

        # Draw prompt
        prompt_surface = self._text_font.render(
            "Press Space or Click to continue",
            True,
            (255, 255, 0)
        )

        prompt_x = logical_width // 2 - prompt_surface.get_width() // 2
        prompt_y = text_rect.bottom + 20

        screen.blit(prompt_surface, (prompt_x, prompt_y))

        padding_x = 20
        padding_y = 12

        self.button_rect = pygame.Rect(
            prompt_x - padding_x,
            prompt_y - padding_y,
            prompt_surface.get_width() + padding_x * 2,
            prompt_surface.get_height() + padding_y * 2
        )

        # Button border
        pygame.draw.rect(screen, (255, 255, 0), self.button_rect, 2)

    ############################################################################
    # Private Methods

    # TODO: Refactor this out into a utils class
    def _draw_wrapped_text(self,
                           surface,
                           text,
                           font,
                           color,
                           rect,
                           line_spacing=4,
                           center=True):
        """!
        @brief Draw word-wrapped text inside a rectangle.
        @param surface Pygame surface to draw on
        @param text String (can contain paragraphs separated by '\n')
        @param font Pygame Font object
        @param color (R, G, B)
        @param rect Pygame.Rect defining text area
        @param line_spacing Extra spacing between lines
        @param center Whether to center text horizontally
        """

        words = []
        for paragraph in text.split("\n"):
            words.append(paragraph.split(" "))
            # paragraph break
            words.append(["\n"])

        x, y = rect.topleft
        max_width = rect.width
        line_height = font.get_linesize()

        line = ""

        for word_list in words:
            if word_list == ["\n"]:
                # render current line before paragraph break
                if line:
                    text_surface = font.render(line, True, color)
                    draw_x = x + (max_width - text_surface.get_width()) // 2 if center else x
                    surface.blit(text_surface, (draw_x, y))
                    y += line_height + line_spacing
                    line = ""
                # extra space for paragraph
                y += line_height
                continue

            for word in word_list:
                test_line = f"{line} {word}".strip()
                test_surface = font.render(test_line, True, color)

                if test_surface.get_width() <= max_width:
                    line = test_line
                else:
                    text_surface = font.render(line, True, color)
                    draw_x = x + (max_width - text_surface.get_width()) // 2 if center else x
                    surface.blit(text_surface, (draw_x, y))
                    y += line_height + line_spacing
                    line = word

        if line:
            text_surface = font.render(line, True, color)
            draw_x = x + (max_width - text_surface.get_width()) // 2 if center else x
            surface.blit(text_surface, (draw_x, y))

################################################################################
