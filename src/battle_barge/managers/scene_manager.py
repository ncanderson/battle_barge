# Standard imports
from __future__ import annotations

# 3rd party imports
import pygame

# Module imports

################################################################################

class SceneManager:
    """!
    @brief Manages the stack of active scenes
    """

    ############################################################################

    def __init__(self):
        """!
        @brief Constructor
        """
        self._stack = []
        self._quit_requested = False

    ############################################################################

    @property
    def current_scene(self):
        """!
        @brief The current scene
        """
        return self._stack[-1] if self._stack else None

    ############################################################################

    @property
    def quit_requested(self):
        """!
        @brief The current scene
        """
        return self._quit_requested

    ############################################################################

    def request_quit(self):
        """!
        @param Allow a scene to request a quit
        """
        print("REQUEST_QUIT")
        self._quit_requested = True

    ############################################################################

    def push(self, scene: SceneBase):
        """!
        @brief Push a new scene on top
        @param scene The new scene to go onto the top of the stack
        """
        self._stack.append(scene)
        scene.on_enter()

    ############################################################################

    def pop(self):
        """!
        @brief Pop the top scene
        """
        if self._stack:
            scene = self._stack.pop()
            scene.on_exit()

    ############################################################################

    def change_scene(self, scene: SceneBase):
        """!
        @brief Replace the entire stack with a new scene
        @param scene The new scene
        """
        while self._stack:
            self.pop()
        self.push(scene)

    ############################################################################

    def handle_input(self, events):
        """!
        @brief Delegate input to top scene
        @param events Event queue
        """
        if self.current_scene:
            self.current_scene.handle_input(events)

    ############################################################################

    def update(self, dt):
        """!
        @brief Update top scene
        @param dt Elapsed time
        """
        if self.current_scene:
            self.current_scene.update(dt)

            # Check for next scene
            if self.current_scene.next_scene:
                self.change(self.current_scene.next_scene)
                self.current_scene.next_scene = None

    ############################################################################

    def draw(self, surface):
        """!
        @brief Draw top scene
        @param surface The surface to drawn to
        """
        if self.current_scene:
            self.current_scene.draw(surface)

################################################################################
