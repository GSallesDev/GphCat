"""Graphical frontend for the mathematical engine.

The engine itself is render-agnostic and can operate
independently from the grafical layer. This module
provides window management, input handling, rendering,
and user interaction.
"""

from typing import Final

from pygame import Surface, Clock
import pygame

from state.app import App
from settings import Settings
from consts import MS2SEC, INIT_FAILNUM

import app


def main() -> None:
    assert pygame.init()[INIT_FAILNUM] == 0, "ERROR: Unable to initialize."

    pygame.display.set_mode(Settings.WINDOW_SIZE)
    pygame.display.set_caption("GphCat")
    pygame.display.set_icon(Surface((16, 16)))

    display: Final[Surface | None] = pygame.display.get_surface()
    assert display, "ERROR: Unable to initialize display."
    App.display = display

    clock: Final[Clock] = Clock()

    assert app.init(), "ERROR: Unable to initialize application."

    while not App.should_close:
        for event in pygame.event.get():
            App.should_close = event.type == pygame.QUIT
            app.handle_event(event)
        app.update(App.dt)
        app.render(App.display)
        pygame.display.update()
        App.dt = clock.tick(Settings.FPS) / MS2SEC

    pygame.quit()


if __name__ == "__main__":
    main()
