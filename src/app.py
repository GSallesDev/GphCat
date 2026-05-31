"""Defines the application lifecycle interface expected by the engine.

The engine invokes these callbacks during initialization,
event processing, update, and rendering stages.

Implementations provide the application-specific behavior,
while scheduling and execution remain under engine control.
"""

from pygame import Surface, Event
import pygame


def init() -> bool:
    return True


def handle_event(event: Event) -> None: ...


def update(dt: float) -> None: ...


def render(display: Surface) -> None:
    display.fill("#181818")
