# Standard imports
from dataclasses import dataclass

# 3rd party imports

# Module imports
from ..utils.game_defs import Difficulty

################################################################################

@dataclass
class GameState:
    """!
    @brief Data for the game state
    """
    player_name: str = "Player 1"

    difficulty: Difficulty = Difficulty.MEDIUM

################################################################################
