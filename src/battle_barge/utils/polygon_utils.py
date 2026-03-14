# Standard imports

# 3rd party imports
import pygame

# Module imports

################################################################################

class PolygonUtils:

    ############################################################################

    @staticmethod
    def handle_polygon_input(events, points):
        """!
        @brief Update polygon points based on input
        @param events
        @param points
        """
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                pos = pygame.mouse.get_pos()
                points.append(pos)
                print(points)

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    points.clear()

                if event.key == pygame.K_BACKSPACE and points:
                    points.pop()

    ############################################################################

    @staticmethod
    def draw_polygon(surface, points):
        """!
        @brief Draw polygon and vertices
        @param surface
        @param points
        """
        if len(points) >= 2:
            pygame.draw.polygon(surface, (255, 255, 0), points, 2)

        for p in points:
            pygame.draw.circle(surface, (255, 0, 0), p, 4)

    ############################################################################

    @staticmethod
    def print_polygon(points):
        """!
        @brief Format and print points
        @param points The list of points to format and print
        """
        print("[", ", ".join(f"({x},{y})" for x,y in points), "]")

################################################################################
