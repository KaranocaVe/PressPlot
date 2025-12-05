import os

import matplotlib.font_manager as fm
import numpy as np
from PIL import Image, ImageOps


def register_fonts():
    """
    Recursively loads all .ttf and .otf fonts from the plottheme/fonts directory.
    """
    # Get the directory where this file is located
    current_dir = os.path.dirname(os.path.abspath(__file__))
    fonts_dir = os.path.join(current_dir, 'fonts')

    if not os.path.exists(fonts_dir):
        # If fonts directory doesn't exist (e.g. not installed correctly), skip
        return

    fonts_found = []
    for root, dirs, files in os.walk(fonts_dir):
        for file in files:
            if file.lower().endswith(('.ttf', '.otf')):
                font_path = os.path.join(root, file)
                try:
                    fm.fontManager.addfont(font_path)
                    fonts_found.append(file)
                except Exception as e:
                    print(f"Warning: Could not load font {file}: {e}")

    if fonts_found:
        print(f"Registered {len(fonts_found)} fonts from {fonts_dir}")


def add_border(input_image, output_image, border_color='#F1F0EA', border_width=80):
    """
    Adds a solid color border to an image using Pillow.
    
    Args:
        input_image: Path to input image.
        output_image: Path to save output image.
        border_color: Color of the border (hex or name). Default is beige.
        border_width: Width of the border in pixels.
    """
    try:
        img = Image.open(input_image)
        img_with_border = ImageOps.expand(img, border=border_width, fill=border_color)
        img_with_border.save(output_image)
        print(f"Added {border_width}px {border_color} border. Saved to {output_image}")
    except Exception as e:
        print(f"Error adding border: {e}")


def save_clean_modern_style(fig, filename, border_width=80, border_color='#F1F0EA', **kwargs):
    """
    Saves a matplotlib figure with the Clean Modern style border.
    
    Args:
        fig: The matplotlib Figure object.
        filename: Output filename.
        border_width: Width of the border in pixels.
        border_color: Color of the border.
        **kwargs: Additional arguments passed to fig.savefig.
    """
    # Save to a temporary file first if we are overwriting or just use the filename
    # But add_border reads and writes. 
    # If we write to filename, then read from filename, and write to filename, it works.

    # We can just save directly to the target first
    fig.savefig(filename, **kwargs)

    # Then add border and overwrite
    add_border(filename, filename, border_color=border_color, border_width=border_width)


def label_line(ax, line, label, x=None, y=None, color=None, **kwargs):
    """
    Add a label to a line plot with matching color.
    
    Args:
        ax: The axes object.
        line: The line object (result of ax.plot).
        label: The text label.
        x: The x coordinate for the label. If None, uses the last x value of the line.
        y: The y coordinate for the label. If None, interpolates the y value at x.
        color: Text color. If None, uses the line's color.
        **kwargs: Additional keyword arguments passed to ax.text.
    """
    # Get line data
    xdata = line.get_xdata()
    ydata = line.get_ydata()

    if x is None:
        x = xdata[-1]
        y = ydata[-1]
    elif y is None:
        # Simple interpolation (assuming sorted x)
        y = np.interp(x, xdata, ydata)

    if color is None:
        color = line.get_color()

    ax.text(x, y, label, color=color, **kwargs)


def draw_dot_grid(ax, x_ticks, y_ticks, color='#d4d4d4', size=10, zorder=0):
    """
    Draws a grid of dots instead of lines.
    
    Args:
        ax: The axes object.
        x_ticks: List or array of X coordinates for the dots.
        y_ticks: List or array of Y coordinates for the dots.
        color: Color of the dots.
        size: Size of the dots.
        zorder: Z-order of the grid (default 0, behind plots).
    """
    # Create a meshgrid of points
    xx, yy = np.meshgrid(x_ticks, y_ticks)
    ax.scatter(xx, yy, color=color, s=size, zorder=zorder, marker='o', edgecolors='none')
