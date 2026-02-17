# Module declaration. Any additional files/classes that are
# added should be included here to facilitate discovery elsewhere

from .main_menu_scene import MainMenuScene
from .new_game_scene import NewGameScene
from .scene_base import SceneBase

__all__ = [
    "MainMenuScene",
    "NewGameScene",
    "SceneBase"
]
