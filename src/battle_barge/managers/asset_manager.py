# Standard imports
from pathlib import Path

# 3rd party imports
import pygame

# Module imports


################################################################################

class AssetManager:
    """!
    @brief Manager to handle access to external resources
    """

    ############################################################################

    def __init__(self, root_dir: Path):
        """!
        @brief Constructor
        @param root_dir Path to the root of the assets directory
        """
        self._root_dir = root_dir
        self._assets_dir = root_dir / "assets"

        # Fonts
        self._fonts_dir = self._assets_dir / "fonts"
        self._font_paths = {}
        self._fonts = {}
        self._load_font_paths()

        # Images
        self._images_dir = self._assets_dir / "images"
        self._images = {}

        # Sounds
        self._sounds_dir = self._assets_dir / "sounds"
        self._sounds = {}


    ############################################################################
    # Public Methods

    def get_font(self, name: str, size: int) -> pygame.font.Font:
        """!
        @brief Get a font managed by this class
        @details This function will use the provided font path object to locate
        the font file, and return either:
        - A newly font object, using this name and size
        - A previously created font object
        @param name The name of the font
        @param size The font size
        @return A constructed pygame.font.Font
        """
        key = (name, size)
        if key not in self._fonts:
            font_path = self._font_paths[name]
            self._fonts[key] = pygame.font.Font(str(font_path), size)
        return self._fonts[key]

    ############################################################################
    # Private Methods

    def _load_font_paths(self) -> None:
        """!
        @brief Load font paths from disk
        @details This helper manages file paths, so other functions in this class
        don't need to know where to locate files. The 'fonts' dict will create
        pygame.font.Font objects as requested, caching them to minimize disk
        trips but allow retrieval as necessary by size.
        """
        # Loading fonts like this for now, but there is a Python library that
        # can extract metadata from a ttf: from fontTools.ttLib import TTFont
        # This function should be expanded to recursively search the 'fonts'
        # directory, and populate self._fonts with the discovered names of
        # each found .ttf file.
        self._font_paths["kingthings-spike"] = self._fonts_dir / "kingthings-spike-font" / "KingthingsSpike-9X6Z.ttf"

    ############################################################################

    def _load_all_images(self) -> None:
        """!
        @brief Load all images from the assets directory
        """
        pass

    ############################################################################

    def _load_all_images(self) -> None:
        """!
        @brief Load all images from the assets directory
        """
        pass

    # ############################################################################

    # # Images
    # def load_image(self, name: str) -> pygame.Surface:
    #     if name not in self.images:
    #         image_path = self.assets_dir / name
    #         self.images[name] = pygame.image.load(str(image_path)).convert_alpha()
    #     return self.images[name]

    # ############################################################################

    # # Sounds
    # def load_sound(self, name: str) -> pygame.mixer.Sound:
    #     if name not in self.sounds:
    #         sound_path = self.assets_dir / name
    #         self.sounds[name] = pygame.mixer.Sound(str(sound_path))
    #     return self.sounds[name]

################################################################################
