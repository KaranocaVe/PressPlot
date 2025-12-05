import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    plottheme.load_theme("clean_modern")

    # Colors
    palette = plottheme.themes.CLEAN_MODERN_NOBEL_PALETTE
    line_color = palette["line_color"]
    fill_color = palette["fill_color"]
    text_color = palette["text_color"]

    fig, ax = plt.subplots(figsize=(12, 7))

    # Data Generation (Time Series)
    years = np.arange(1910, 2025)

    # Synthetic data
    values = []
    for y in years:
        if y < 1920:
            val = 25 + np.random.normal(0, 2)
        elif y < 1935:
            val = 12 + np.random.normal(0, 2)
        elif y < 1945:
            val = 12 + (y - 1935) * 1.5 + np.random.normal(0, 2)
        elif y < 1990:
            val = 30 + np.random.normal(0, 3)
        elif y < 2005:
            val = 30 - (y - 1990) * 0.6 + np.random.normal(0, 2)
        elif y < 2016:
            val = 22 + (y - 2005) * 1.5 + np.random.normal(0, 2)
        else:
            val = 38 - (y - 2016) * 0.6 + np.random.normal(0, 2)
        values.append(val)

    values = np.array(values)

    # Smoothing
    window_size = 3
    weights = np.repeat(1.0, window_size) / window_size
    values_smooth = np.convolve(values, weights, 'same')
    values_smooth[0] = values[0]
    values_smooth[-1] = values[-1]

    # Plot Line
    ax.plot(years, values_smooth, color=line_color, linewidth=4, zorder=3)

    # Area Fill
    ax.fill_between(years, 0, values_smooth, color=fill_color, alpha=0.8, zorder=2)

    # Grid
    ax.grid(axis='y', color='#d4d4d4', linewidth=1.5, zorder=0)
    ax.grid(axis='x', visible=False)

    # Axes Config
    ticks = [1910, 1930, 1950, 1970, 1990, 2010, 2024]
    labels = ["1910", "30", "50", "70", "90", "2010", "24"]

    ax.set_xticks(ticks)
    ax.set_xticklabels(labels, fontsize=24, fontweight='normal')
    ax.tick_params(axis='x', which='major', length=10, width=2, color='black', direction='out')

    # Y-Axis
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.set_yticklabels(["0", "10", "20", "30", "40"], fontsize=24, fontweight='normal')
    ax.tick_params(axis='y', labelleft=False, labelright=True, length=0)

    ax.set_ylim(0, 45)
    ax.set_xlim(1910, 2024)

    # Spines
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['bottom'].set_color('black')

    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Layout Strategy:
    # Use fig.text for all header elements to ensure absolute positioning and avoid overlap

    # FORCE Layout using ax.set_position to strictly define chart area
    # [left, bottom, width, height]
    # top = bottom + height = 0.15 + 0.50 = 0.65
    # This leaves 35% of the figure height for the header!
    ax.set_position([0.05, 0.15, 0.85, 0.50])

    # 1. Main Title (y=0.95)
    fig.text(0.05, 0.95, "Scientific Nobel laureates,",
             fontsize=28, fontweight='bold', ha='left', va='top', color=text_color)

    # 2. Subtitle (y=0.85)
    fig.text(0.05, 0.85, "% born outside the country they represented",
             fontsize=28, fontweight='bold', ha='left', va='top', color=text_color)

    # Save
    final_file = "reproduce_nobel.png"
    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
