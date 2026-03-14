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

        self._scene_background_image = asset_manager.get_image("galaxy-large")

        # Points of the areas we're drawing
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
        PolygonUtils.handle_polygon_input(events, self._polygon_points)

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
        self._polygon = [(663, 599), (532, 672), (746, 767), (875, 682)]
        pygame.draw.polygon(screen, (255,255,0), self._polygon, 2)


    ############################################################################
    # Private Methods

################################################################################
