"""Centralized definition of application settings

Provides semantic names for colors, spacing, dimensions,
and other UI-relared values used throughout the application.
"""

from typing import Final
from pygame import Vector2 as Vec2


class Settings:
    WINDOW_SIZE: Vec2 = Vec2(1000, 600)
    FPS: int = 60
    FONT_NAME: str = "JetBrains Mono"

    class GphView:
        GRID_DENSITY: Final[int] = 40
        BACKGROUND_COLOR: Final[str] = "#181818"
        OUTLINE_COLOR_FOCUSED: Final[str] = "#FFFFFF"
        OUTLINE_COLOR_UNFOCUSED: Final[str] = "#555555"
        OUTLINE_SIZE: Final[int] = 1
        POINT_COLOR: Final[str] = "#333333"
        POINT_SIZE: Final[int] = 3
