"""Centralized definition of application settings

Provides semantic names for colors, spacing, dimensions,
and other UI-relared values used throughout the application.
"""

from pygame import Vector2 as Vec2


class Settings:
    WINDOW_SIZE: Vec2 = Vec2(800, 600)
    FPS: int = 60
