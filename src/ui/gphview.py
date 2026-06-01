"""Docs."""

from typing import Final
from pygame import Surface, Event, Rect

from pygame import Vector2 as Vec2
from ui.window import Window
import pygame

from settings import Settings


class GphView:
    def __init__(self, data: dict[str, set[str]], window: Window):
        self.data: dict[str, set[str]] = data
        self.position = Vec2(0, 0)
        self.window: Window = window
        self.bounds: Rect = Rect(
            *self.window.position,
            *self.window.size,
        )
        self.focused: bool = False

        self.moving: bool = False
        self.moving_reference: Vec2 = Vec2(0, 0)

    def handle_event(self, event: Event) -> None:
        self.focused = self.bounds.collidepoint(pygame.mouse.get_pos())

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1 and self.focused:
                self.moving = True
                self.moving_reference = event.pos

        if event.type == pygame.MOUSEBUTTONUP:
            self.moving = False
            self.moving_reference = event.pos

    def update(self, dt: float) -> None:
        if self.moving:
            mouse_pos: Vec2 = Vec2(pygame.mouse.get_pos())
            self.position = mouse_pos - self.moving_reference

    def render(self) -> None:
        # NOTE:
        OUTLINE_COLOR: Final[str] = (
            Settings.GphView.OUTLINE_COLOR_FOCUSED
            if self.focused
            else Settings.GphView.OUTLINE_COLOR_UNFOCUSED
        )

        self.window.surface.fill(Settings.GphView.BACKGROUND_COLOR)

        offset: Vec2 = Vec2(
            self.position.x % Settings.GphView.GRID_DENSITY,
            self.position.y % Settings.GphView.GRID_DENSITY,
        )

        H: int = self.window.surface.height // Settings.GphView.GRID_DENSITY + 2
        W: int = self.window.surface.width // Settings.GphView.GRID_DENSITY + 2
        for y in range(H):
            for x in range(W):
                position = Vec2(x, y) * Settings.GphView.GRID_DENSITY + offset
                pygame.draw.circle(
                    self.window.surface,
                    Settings.GphView.POINT_COLOR,
                    position,
                    Settings.GphView.POINT_SIZE,
                )

        pygame.draw.rect(
            self.window.surface,
            OUTLINE_COLOR,
            (0, 0, *self.window.surface.get_size()),
            Settings.GphView.OUTLINE_SIZE,
        )
