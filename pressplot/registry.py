from typing import Dict

from .core import Theme


class ThemeRegistry:
    """
    A central registry to manage available themes.
    """
    _instance = None
    _themes: Dict[str, Theme] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ThemeRegistry, cls).__new__(cls)
        return cls._instance

    def register(self, theme: Theme):
        """
        Register a new theme.
        """
        if not isinstance(theme, Theme):
            raise TypeError("Argument must be an instance of Theme")
        self._themes[theme.name] = theme

    def get(self, name: str) -> Theme:
        """
        Retrieve a theme by name.
        """
        if name not in self._themes:
            raise KeyError(f"Theme '{name}' not found. Available themes: {list(self._themes.keys())}")
        return self._themes[name]

    def list_themes(self) -> list:
        """
        List all registered theme names.
        """
        return list(self._themes.keys())

    def clear(self):
        """
        Clear all registered themes.
        """
        self._themes.clear()


# Global instance
registry = ThemeRegistry()
