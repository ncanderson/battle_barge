# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports
from ..game_objects import Planet
from ..utils.drawing_utils import DrawingUtils
from ..utils.polygon_utils import PolygonUtils
from .scene_base import SceneBase

################################################################################

class PlanetSelectionScene(SceneBase):
    """!
    @brief New game scene
    """

    ############################################################################

    def __init__(self,
                 app: App = None):
        """!
        @brief Constructor
        @param app
        """
        super().__init__(app)

        self._planets = [
            Planet("Kharzug IX", (615, 298)),
            Planet("Vanthex", (1175, 232)),
            Planet("Dreggor II", (1344, 564)),
            Planet("Skorn Vaal", (1398, 767)),
            Planet("Brakkus Null", (493, 674))
        ]

    ############################################################################
    # Lifecycle hooks

    def on_enter(self):
        """!
        @brief Called when the scene becomes active (pushed or changed)
        """
        print(f"Entering {self.__class__.__name__}")

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
        # Clear
        screen.fill((0,0,0))

        DrawingUtils.draw_fullscreen_background(screen,
                                                self._app.asset_manager,
                                                "galaxy-spiral-arm")

        # Draw debug polygon
        #PolygonUtils.draw_polygon(screen, self._polygon_points)


    ############################################################################
    # Private Methods

################################################################################
