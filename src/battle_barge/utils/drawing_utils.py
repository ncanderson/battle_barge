# Standard imports

# 3rd party imports
import pygame

# Module imports

################################################################################

class DrawingUtils:

    ############################################################################

    @staticmethod
    def draw_fullscreen_background(screen,
                                   asset_manager,
                                   image_name: str) -> None:
        """!
        @brief Draw a fullscreen background image to `screen`
        @param screen The screen to draw to
        @param asset_manager The asset manage that contains the image
        @param image_name The image name, without file extension
        """
        # Get logical surface size
        logical_width, logical_height = screen.get_size()

        # Scale background
        bg_scaled = pygame.transform.scale(asset_manager.get_image(image_name),
                                           (logical_width, logical_height))

        # Draw it
        screen.blit(bg_scaled, (0, 0))

################################################################################
