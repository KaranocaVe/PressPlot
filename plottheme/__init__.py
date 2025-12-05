from typing import List, Optional

from .core import Theme
from .registry import registry
from .themes import clean_modern_theme
from .utils import label_line, save_clean_modern_style, register_fonts, draw_dot_grid


def register_theme(name: str, rc_params: dict, palette: Optional[List] = None):
    """
    Helper function to create and register a theme.
    """
    theme = Theme(name, rc_params, palette)
    registry.register(theme)


def load_theme(name: str):
    """
    Apply a registered theme by name.
    """
    theme = registry.get(name)
    theme.apply()


def get_theme(name: str) -> Theme:
    """
    Get a registered theme object.
    """
    return registry.get(name)


def list_themes() -> list:
    """
    List available themes.
    """
    return registry.list_themes()


# Register default themes
registry.register(clean_modern_theme)

# Automatically register local fonts
register_fonts()

__all__ = ["Theme", "register_theme", "load_theme", "get_theme", "list_themes", "label_line", "save_clean_modern_style",
           "draw_dot_grid"]
