"""Docs."""

from pygame import Surface


class App:
    display: Surface
    should_close: bool = False
    dt: float = 0.0
