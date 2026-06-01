"""Docs."""

from typing import Optional
from enum import IntEnum, auto
from pygame import Font, Surface
from pygame import Vector2 as Vec2
import pygame

from settings import Settings


class FontSize(IntEnum):
    F8 = auto()
    F16 = auto()
    F32 = auto()
    F64 = auto()


class FontAlign(IntEnum):
    NONE = auto()
    # UR
    # DL
    # DR
    CENTER = auto()


class State:
    fonts: dict[FontSize, Font] = {}


def init() -> bool:
    # PROTOTYPE
    State.fonts[FontSize.F8] = pygame.font.SysFont(Settings.FONT_NAME, 8)
    State.fonts[FontSize.F16] = pygame.font.SysFont(Settings.FONT_NAME, 16)
    State.fonts[FontSize.F32] = pygame.font.SysFont(Settings.FONT_NAME, 32)
    State.fonts[FontSize.F64] = pygame.font.SysFont(Settings.FONT_NAME, 64)
    return True


def text_size(text: str, size: FontSize) -> Vec2:
    assert size in State.fonts, "ERROR: Unexistent font size."
    return Vec2(State.fonts[size].size(text))


def render(
    display: Surface,
    text: str,
    position: Vec2 | tuple[float, float],
    size: FontSize,
    color: str,
    align: Optional[FontAlign] = None,
):
    assert size in State.fonts, "ERROR: Unexistent font size."
    if align == FontAlign.CENTER:
        position -= text_size(text, size) / 2

    display.blit(State.fonts[size].render(text, True, color), position)
