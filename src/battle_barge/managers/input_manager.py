# Standard imports
import pygame

# 3rd party imports

# Module imports
from battle_barge.managers import InputManager

################################################################################

class InputManager:
    """!
    @brief Class to manage user inputs
    """

    ############################################################################

    def __init__(self):
        """!
        @brief Constructor
        """
        self._commands = []

    ############################################################################

    def update(self, events) -> None:
        """!
        @brief Process pygame events and generate game commands
        @param events Pygame events
        """
        # Wipe previous commands
        self._commands.clear()

        # Handle new ones
        for event in events:
            if event.type == pygame.QUIT:
                self._commands.append(("quit", None))
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self._commands.append(("quit", None))
                elif event.key == pygame.K_u:  # undo
                    self._commands.append(("undo", None))
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # left click
                    pos = event.pos
                    self._commands.append(("place_stone", pos))

    ############################################################################

    def get_commands(self) -> list[str]:
        """!
        @brief Get all commands
        """
        return list(self._commands)

################################################################################
