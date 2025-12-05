from .core import Theme

# Clean Modern Style Definition
CLEAN_MODERN_RC = {
    # Background
    "figure.facecolor": "#F1F0EA",
    "axes.facecolor": "#F1F0EA",
    "savefig.facecolor": "#F1F0EA",

    # Grid
    "axes.grid": True,
    "grid.color": "#d4d4d4",  # Sampled from image
    "grid.linestyle": "-",
    "grid.linewidth": 1.5,  # Slightly thicker
    "grid.alpha": 1.0,
    "axes.axisbelow": True,

    # Axes Spines
    "axes.spines.left": False,
    "axes.spines.right": False,
    "axes.spines.top": False,
    "axes.spines.bottom": True,
    "axes.edgecolor": "#1B1919",
    "axes.linewidth": 2.0,

    # Ticks and Labels
    "xtick.bottom": True,
    "xtick.top": False,
    "ytick.left": False,
    "ytick.right": False,
    "ytick.labelleft": False,
    "ytick.labelright": True,
    "xtick.major.size": 5,
    "xtick.minor.size": 0,
    "ytick.major.size": 0,
    "xtick.direction": "out",

    # Fonts
    # We provide a stack of condensed/robust sans-serif fonts.
    "font.family": "sans-serif",
    "font.weight": "bold",
    "font.sans-serif": [
        "Swift",  # Will match the loaded font family name
        "ITC Officina Sans",
        "Officina Sans",
        "DIN Condensed",
        "Avenir Next Condensed",
        "Roboto Condensed",
        "Arial Narrow",
        "Helvetica Neue",
        "Verdana",
        "Arial",
        "sans-serif"
    ],
    "text.color": "#1B1919",
    "axes.labelcolor": "#1B1919",
    "xtick.color": "#1B1919",
    "ytick.color": "#1B1919",
    "axes.titlesize": 24,
    "axes.titleweight": "bold",
    "axes.titlelocation": "left",
    "axes.labelsize": 20,
    "axes.labelweight": "bold",
    "xtick.labelsize": 18,
    "ytick.labelsize": 18,
    "axes.unicode_minus": False,

    # Lines
    "lines.linewidth": 2.5,
    "lines.solid_capstyle": "round",

    # Legend
    "legend.frameon": False,
    "legend.numpoints": 1,
    "legend.scatterpoints": 1,
}

# Colors sampled from reference image
CLEAN_MODERN_PALETTE = [
    "#E62A24",  # Red
    "#B6B6A9",  # Grey - Warm grey
    "#F7A493",  # Pink
    "#00A5C6",  # Cyan
    "#0C5DA5",  # Dark Blue
    "#FF9500",  # Orange
]

# Gradient Map Colors (Light Pink -> Dark Red -> Very Dark Red)
CLEAN_MODERN_MAP_PALETTE = [
    "#FDDBC7",  # Light Pink/Beige
    "#F4A582",  # Soft Red
    "#D6604D",  # Medium Red
    "#B2182B",  # Deep Red
    "#67001F",  # Very Dark Red
    "#000000"  # Black
]

# Manufacturing Chart Palette
CLEAN_MODERN_MANUFACTURING_PALETTE = [
    "#3B5A9D",  # Blue (Germany)
    "#FA9B85",  # Salmon/Pink (Britain)
    "#7F7F7F",  # Grey (US)
    "#E62A24",  # Red (China) - Same as main red
]

# Diverging Chart Palette (Shutdown Chart)
CLEAN_MODERN_DIVERGING_PALETTE = {
    "blue_text": "#4A6FA5",
    "red_text": "#F05A45",
    "bg_left": "#E8ECEF",  # Light Blue-Grey
    "bg_right": "#F9EBE8",  # Light Red-Beige
    "dot_color": "#1B1919"
}

# TikTok Treemap Palette
CLEAN_MODERN_TIKTOK_PALETTE = {
    "red": "#EE4C3D",  # Bright Red/Coral
    "pink": "#F8B195",  # Salmon/Peach
    "grey": "#D6D6CE",  # Light Grey/Greenish
    "border": "#000000",  # Black borders
    "bg": "#F1F0EA"  # Background
}

# Temperature Bubble Chart Palette (Blue -> Red)
CLEAN_MODERN_TEMPERATURE_PALETTE = [
    "#2A4B7C",  # Deep Blue (London)
    "#5C80B0",  # Mid Blue
    "#A4B9D6",  # Light Blue
    "#E8DCCA",  # Neutral/Beige
    "#F5AFA6",  # Light Red
    "#EB6052",  # Mid Red
    "#D92E27",  # Deep Red (Madrid/Milan)
]

# Scatter Plot Palette (Government Effectiveness)
CLEAN_MODERN_SCATTER_PALETTE = {
    "dot_color": "#F08C84",  # Salmon Pink/Red
    "line_color": "#E62A24",  # Bright Red
    "text_color": "#1B1919",
    "highlight_stroke": "#1B1919"
}

# Tariff Bar Chart Palette
CLEAN_MODERN_TARIFF_PALETTE = {
    "2024_rate": "#F4A598",  # Light Pink/Salmon
    "increase": "#E62A24",  # Bright Red
    "text_color": "#1B1919"
}

# Nobel Line Chart Palette
CLEAN_MODERN_NOBEL_PALETTE = {
    "line_color": "#E62A24",  # Bright Red
    "fill_color": "#F2CDC3",  # Light reddish beige
    "text_color": "#1B1919"
}

# Tech Index Chart Palette
CLEAN_MODERN_TECH_PALETTE = {
    "highlight_red": "#E62A24",  # Bright Red
    "light_red": "#F08C84",  # Lighter red for lines/dots
    "grey_dot": "#B6B6A9",  # Warm grey for "Other"
    "text_color": "#1B1919"
}

# Register standard colormaps
import matplotlib.colors
from matplotlib.colors import LinearSegmentedColormap, ListedColormap

# Continuous
clean_modern_reds = LinearSegmentedColormap.from_list("clean_modern_reds", CLEAN_MODERN_MAP_PALETTE)
# Handle different Matplotlib versions safely
if hasattr(matplotlib, 'colormaps'):
    try:
        matplotlib.colormaps.register(clean_modern_reds)
    except ValueError:
        pass  # Already registered
elif hasattr(matplotlib.cm, 'register_cmap'):
    getattr(matplotlib.cm, 'register_cmap')(cmap=clean_modern_reds)

# Discrete (for map buckets)
clean_modern_reds_discrete = ListedColormap(CLEAN_MODERN_MAP_PALETTE, name="clean_modern_reds_discrete")
if hasattr(matplotlib, 'colormaps'):
    try:
        matplotlib.colormaps.register(clean_modern_reds_discrete)
    except ValueError:
        pass
elif hasattr(matplotlib.cm, 'register_cmap'):
    getattr(matplotlib.cm, 'register_cmap')(cmap=clean_modern_reds_discrete)

# Temperature Diverging
clean_modern_temp = LinearSegmentedColormap.from_list("clean_modern_temp", CLEAN_MODERN_TEMPERATURE_PALETTE)
if hasattr(matplotlib, 'colormaps'):
    try:
        matplotlib.colormaps.register(clean_modern_temp)
    except ValueError:
        pass
elif hasattr(matplotlib.cm, 'register_cmap'):
    getattr(matplotlib.cm, 'register_cmap')(cmap=clean_modern_temp)

clean_modern_theme = Theme("clean_modern", CLEAN_MODERN_RC, CLEAN_MODERN_PALETTE)
