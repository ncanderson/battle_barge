# Standard imports
from dataclasses import dataclass, field
from typing import Optional

# 3rd party imports
import pygame

# Module imports

################################################################################

@dataclass(kw_only=True)
class Planet:
    """!
    @brief Dataclass to manage a given planet
    """
    # @brief Planet name
    name: str

    # @brief Screen coords
    coords: tuple[int, int]

    # @brief Optional on-hover tooltip
    tooltip: Optional[str] = None

    # @brief Planet radius
    radius: int = 20

    # @brief Mouse is hovering over the planet coords
    is_hovered: bool = field(default=False, init=False)

    # @brief Planet name
    rect: pygame.Rect = field(init=False)

    def __post_init__(self):
        """!
        @brief This can be used to populate anything after the ctor runs
        """
        # A rect around the center of the planet, useful for centering
        x, y = self.coords
        self.rect = pygame.Rect(x - self.radius,
                                y - self.radius,
                                self.radius * 2,
                                self.radius * 2)

    ############################################################################

    def update_hover(self, mouse_pos):
        """!
        @brief Check for hover collision from mouse position
        """
        # Unpack mouse position
        mx, my = mouse_pos
        # Vector from planet center to the mouse position
        dx = mx - self.coords[0]
        dy = my - self.coords[1]
        # Collision detection
        self.is_hovered = (dx * dx + dy * dy) <= (self.radius * self.radius)

    ############################################################################

    def draw(self, screen, planet_img, font):
        # draw planet
        img = planet_img
        if self.is_hovered:
            # optionally, you can tint the image or use a different hover image
            img = pygame.transform.scale(planet_img, (self.radius*2+4, self.radius*2+4))
        rect = img.get_rect(center=self.pos)
        screen.blit(img, rect)

        # draw tooltip if hovered
        if self.is_hovered and self.tooltip:
            text_surface = font.render(self.tooltip, True, (255, 255, 255))
            padding = 4
            box_rect = text_surface.get_rect(topleft=(rect.right + 8, rect.top))
            box_rect.inflate_ip(padding*2, padding*2)
            pygame.draw.rect(screen, (0,0,0), box_rect)
            pygame.draw.rect(screen, (255,255,255), box_rect, 1)
            screen.blit(text_surface, (box_rect.x + padding, box_rect.y + padding))

################################################################################
