# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports
from ..game_objects.planet import Planet
from ..utils.drawing_utils import DrawingUtils
from ..utils.shape_utils import ShapeUtils
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
            Planet(name="Kharzug IX", coords=(615, 298)),
            Planet(name="Vanthex", coords=(1175, 232)),
            Planet(name="Dreggor II", coords=(1344, 564)),
            Planet(name="Skorn Vaal", coords=(1398, 767)),
            Planet(name="Brakkus Null", coords=(493, 674))
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
        ShapeUtils.handle_polygon_input(events, self._polygon_points)

        mouse_pos = pygame.mouse.get_pos()
        for planet in self._planets:
            planet.update_hover(mouse_pos)

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

        for planet in self._planets:
            planet.draw(screen, self._planet_img, self._text_font)

        # Draw debug polygon
        #ShapeUtils.draw_polygon(screen, self._polygon_points)


    ############################################################################
    # Private Methods

################################################################################
