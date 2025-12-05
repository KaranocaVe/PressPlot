from copy import deepcopy
from typing import Dict, Optional, List, Any

import matplotlib as mpl
import matplotlib.pyplot as plt


class Theme:
    """
    Represents a plot theme configuration.
    
    A Theme encapsulates matplotlib rcParams and a color cycle/palette.
    It allows for validation and application of these settings.
    """

    def __init__(self, name: str, rc_params: Dict[str, Any], palette: Optional[List[str]] = None):
        """
        Initialize a Theme.

        Args:
            name (str): The name of the theme.
            rc_params (Dict[str, Any]): Dictionary of matplotlib rcParams.
            palette (Optional[List[str]]): List of color hex codes or names. 
                                           If provided, it overrides axes.prop_cycle.
        """
        self.name = name
        self._rc_params = deepcopy(rc_params)
        self._palette = deepcopy(palette) if palette else []

        self._validate()

    def _validate(self):
        """
        Validate the theme configuration.
        """
        # Basic validation can be expanded here.
        # For now, we just ensure palette is a list if provided.
        if not isinstance(self._palette, list):
            raise ValueError(f"Palette must be a list of colors, got {type(self._palette)}")

    @property
    def rc_params(self) -> Dict[str, Any]:
        return self._rc_params

    @property
    def palette(self) -> List[str]:
        return self._palette

    def apply(self):
        """
        Apply this theme to the current matplotlib session.
        """
        # 1. Update rcParams
        plt.rcParams.update(self._rc_params)

        # 2. Apply color cycle if palette exists
        if self._palette:
            mpl.rcParams['axes.prop_cycle'] = mpl.cycler(color=self._palette)

    def to_dict(self) -> Dict[str, Any]:
        """
        Serialize theme to a dictionary.
        """
        return {
            "name": self.name,
            "rc_params": self._rc_params,
            "palette": self._palette
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Theme':
        """
        Create a Theme instance from a dictionary.
        """
        return cls(
            name=data.get("name", "unnamed"),
            rc_params=data.get("rc_params", {}),
            palette=data.get("palette", None)
        )
