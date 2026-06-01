"""Defines the application lifecycle interface expected by the engine.

The engine invokes these callbacks during initialization,
event processing, update, and rendering stages.

Implementations provide the application-specific behavior,
while scheduling and execution remain under engine control.
"""

from settings import Settings

from typing import Final
from pygame import Vector2 as Vec2
from pygame import Surface, Event, Rect
import pygame

from ui.fontdraw import FontSize
import ui.fontdraw as fontdraw

from ui.window import Window
from ui.gphview import GphView

LAYOUT0_HORIZONTAL_PC: Final[float] = 0.60
LAYOUT1_HORIZONTAL_PC: Final[float] = 0.50
LAYOUT0_VERTICAL_PC: Final[float] = 0.60


class State:
    window_gph0: Window = Window(
        Vec2(0, 0),
        Vec2(
            Settings.WINDOW_SIZE.x * LAYOUT0_HORIZONTAL_PC * LAYOUT1_HORIZONTAL_PC,
            Settings.WINDOW_SIZE.y * LAYOUT0_VERTICAL_PC,
        ),
    )
    window_gph1: Window = Window(
        Vec2(Settings.WINDOW_SIZE.x * LAYOUT0_HORIZONTAL_PC * LAYOUT1_HORIZONTAL_PC, 0),
        Vec2(
            Settings.WINDOW_SIZE.x * LAYOUT0_HORIZONTAL_PC * LAYOUT1_HORIZONTAL_PC,
            Settings.WINDOW_SIZE.y * LAYOUT0_VERTICAL_PC,
        ),
    )
    window_gph_out: Window = Window(
        Vec2(Settings.WINDOW_SIZE.x * LAYOUT0_HORIZONTAL_PC, 0),
        Vec2(
            Settings.WINDOW_SIZE.x * (1 - LAYOUT0_HORIZONTAL_PC),
            Settings.WINDOW_SIZE.y,
        ),
    )

    window_menu: Window = Window(
        Vec2(
            0,
            Settings.WINDOW_SIZE.y * LAYOUT0_VERTICAL_PC,
        ),
        Vec2(
            Settings.WINDOW_SIZE.x * LAYOUT0_HORIZONTAL_PC,
            Settings.WINDOW_SIZE.y * (1 - LAYOUT0_VERTICAL_PC),
        ),
    )

    gph0_view: GphView
    gph1_view: GphView
    gph_out_view: GphView


def init() -> bool:
    State.gph0_view = GphView(
        {
            "A": {"B", "C"},
            "B": {"A"},
            "C": {"A"},
        },
        State.window_gph0,
    )
    State.gph1_view = GphView({"1": {"2"}, "2": {"3"}, "3": {"2"}}, State.window_gph1)
    State.gph_out_view = GphView(
        {"1": {"2"}, "2": {"3"}, "3": {"2"}}, State.window_gph_out
    )

    return fontdraw.init()


def handle_event(event: Event) -> None:
    State.gph0_view.handle_event(event)
    State.gph1_view.handle_event(event)
    State.gph_out_view.handle_event(event)


def update(dt: float) -> None:
    State.gph0_view.update(dt)
    State.gph1_view.update(dt)
    State.gph_out_view.update(dt)


def render(display: Surface) -> None:
    State.gph0_view.render()
    State.window_gph0.render(display)

    State.gph1_view.render()
    State.window_gph1.render(display)

    State.gph_out_view.render()
    State.window_gph_out.render(display)
