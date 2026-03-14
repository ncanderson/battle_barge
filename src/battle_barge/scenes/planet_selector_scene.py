# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports
from .scene_base import SceneBase
from ..utils.polygon_utils import PolygonUtils

################################################################################

class PlanetSelectorScene(SceneBase):
    """!
    @brief Planet (and difficulty) selection scene
    """

    ############################################################################

    def __init__(self,
                 scene_manager: SceneManager,
                 asset_manager: AssetManager):
        """!
        @brief Constructor
        @param assets Instance of the AssetManager
        """
        super().__init__(scene_manager, asset_manager)

        # Set the necessary manager attributes
        self._scene_manager = scene_manager
        self._asset_manager = asset_manager

        # Mouse positio
        self._mouse_pos = None

        # Background image
        self._scene_background_image = asset_manager.get_image("galaxy-large")

        # Start zones
        self._easy_zone = [(506, 640), (625, 591), (742, 639), (684, 747)]
        self._med_zone = [(788, 662), (758, 757), (898, 785), (924, 695)]
        self._hard_zone = [(658, 584), (693, 541), (856, 609), (796, 650)]

        # All zones collected for ease of looping
        # TODO make a separate class for the zones
        self._zones = [
            {
                "name": "Central Space",
                "difficulty": "Easy",
                "polygon": self._easy_zone
            },
            {
                "name": "Spiral Arm",
                "difficulty": "Medium",
                "polygon": self._med_zone
            },
            {
                "name": "Galactic Core",
                "difficulty": "Hard",
                "polygon": self._hard_zone
            }
        ]

        # Storage for the zone under the mouse
        self._hovered_zone = None

        # Empty vector to use in conjunction with the drawing tools
        self._polygon_points = []

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
        # Used for collecting points when figuring out where polygons should be
        #PolygonUtils.handle_polygon_input(events, self._polygon_points)

        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                # This bit relies on the update function to determine which
                # polygon that click is in
                if self._hovered_zone:
                    print("Selected:", self._hovered_zone["name"])

    ############################################################################

    def update(self, dt):
        """!
        @brief Handle updates
        @param dt Delta time - total elapsed time
        """
        # Check for hover zone
        self._mouse_pos = pygame.mouse.get_pos()

        # Reset the hovered zone for this frame
        self._hovered_zone = None

        for zone in self._zones:
            if PolygonUtils.point_in_polygon(self._mouse_pos, zone["polygon"]):
                self._hovered_zone = zone
                break

    ############################################################################

    def draw(self, screen):
        """!
        @brief Re-draw the scene
        @param screen Game screen to draw to
        """
        # Get logical surface size
        logical_width, logical_height = screen.get_size()

        # Galaxy background
        background = self._asset_manager.get_image("galaxy-large")
        # Scale background
        bg_scaled = pygame.transform.scale(background,
                                          (logical_width, logical_height))

        # Draw it
        screen.blit(bg_scaled, (0, 0))

        # Draw debug polygon
        #PolygonUtils.draw_polygon(screen, self._polygon_points)

        # The starting zones, checking for a zone under the mouse
        for zone in self._zones:
            color = (0,255,0) if zone == self._hovered_zone else (255,255,0)
            pygame.draw.polygon(screen, color, zone["polygon"], 2)

        if self._hovered_zone:
            tooltip_text = f"{self._hovered_zone['difficulty']}:\n{self._hovered_zone['name']}"
            text_surface = self._text_font.render(tooltip_text, True, (255,255,255))
            mx, my = self._mouse_pos
            padding = 6
            bg_rect = text_surface.get_rect(topleft=(mx + 10, my + 10))
            bg_rect.inflate_ip(padding * 2, padding * 2)
            pygame.draw.rect(screen, (0,0,0), bg_rect)
            pygame.draw.rect(screen, (255,255,255), bg_rect, 1)
            screen.blit(text_surface, (bg_rect.x + padding, bg_rect.y + padding))

    ############################################################################
    # Private Methods

################################################################################
