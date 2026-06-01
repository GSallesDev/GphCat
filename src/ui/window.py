"""Docs."""

from dataclasses import dataclass, field
from pygame import Surface
from pygame import Vector2 as Vec2


@dataclass
class Window:
    position: Vec2
    size: Vec2
    surface: Surface = field(init=False)

    def __post_init__(self):
        self.surface = Surface(self.size)

    def render(self, display: Surface) -> None:
        display.blit(self.surface, self.position)
