import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import pressplot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pressplot


def main():
    pressplot.load_theme("clean_modern")

    # Data
    categories = ["Republican", "Independent", "Democrat"]
    values = [-65, 25, 78]  # Net blame

    # Colors (approximated from image)
    # Use theme palette
    palette = pressplot.themes.CLEAN_MODERN_DIVERGING_PALETTE

    # Text Colors
    blue_text = palette["blue_text"]
    red_text = palette["red_text"]

    # Background Shading Colors
    bg_left = palette["bg_left"]  # Light Blue-Grey
    bg_right = palette["bg_right"]  # Light Red-Beige

    # Dot/Line Color
    dot_color = palette["dot_color"]  # Black/Dark Grey

    fig, ax = plt.subplots(figsize=(10, 7))  # Increased height

    # 1. Background Shading
    ax.axvspan(-100, 0, facecolor=bg_left, alpha=1.0, zorder=0)
    ax.axvspan(0, 100, facecolor=bg_right, alpha=1.0, zorder=0)

    # 2. Grid
    ax.grid(axis='x', color='#d4d4d4', linewidth=1.5, zorder=1)
    ax.grid(axis='y', visible=False)

    # 3. Zero Line
    ax.axvline(0, color='black', linewidth=2.5, zorder=2)

    # 4. Lollipop Plot
    y_pos = np.arange(len(categories))

    # Draw lines (hlines)
    ax.hlines(y=y_pos, xmin=0, xmax=values, color=dot_color, linewidth=3.5, zorder=3)

    # Draw dots
    ax.scatter(values, y_pos, color=dot_color, s=250, zorder=4, edgecolors='none')

    # 5. Axes Config
    # Force labels to the left
    ax.tick_params(axis='y', labelleft=True, labelright=False)

    ax.set_yticks(y_pos)
    ax.set_yticklabels(categories, fontsize=20, fontweight='bold')

    # X-axis at the top
    ax.xaxis.tick_top()
    ax.xaxis.set_label_position('top')

    ax.set_xlim(-80, 80)
    ax.set_xticks([-80, -40, 0, 40, 80])
    ax.set_xticklabels(["-80", "-40", "0", "40", "80"], fontsize=20, fontweight='bold')

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Remove tick marks but keep labels
    ax.tick_params(axis='x', length=0, pad=10)
    ax.tick_params(axis='y', length=0, pad=10)

    # 6. Text Annotations
    # Use fig.text for all header elements to ensure absolute positioning and avoid overlap

    # Layout Strategy:
    # 1. Main Title at top
    # 2. Subtitle below title
    # 3. Column headers below subtitle
    # 4. Chart area below headers

    # FORCE Layout using ax.set_position to strictly define chart area
    # [left, bottom, width, height]
    # top = bottom + height = 0.1 + 0.50 = 0.60
    # This leaves 40% of the figure height for the header!
    ax.set_position([0.25, 0.1, 0.7, 0.50])

    # 1. Main Title (y=0.96)
    fig.text(0.5, 0.96, "“Who is to blame the most for the government shutdown?”",
             ha='center', va='top', fontsize=24, fontweight='bold', color='#1B1919')

    # 2. Subtitle (y=0.88)
    fig.text(0.5, 0.88, "Net blame, Oct 6th 2025, percentage points",
             ha='center', va='top', fontsize=20, fontweight='normal', color='#1B1919')

    # 3. Column Headers (y=0.78)
    # Calculated based on layout: left=0.25, width=0.7
    # Left header x: 0.25 + 0.7*0.25 = 0.425
    # Right header x: 0.25 + 0.7*0.75 = 0.775

    fig.text(0.425, 0.78, "Blame Dems more", color=blue_text,
             fontsize=20, fontweight='bold', ha='center', va='bottom')

    fig.text(0.775, 0.78, "Blame Reps more", color=red_text,
             fontsize=20, fontweight='bold', ha='center', va='bottom')

    # Save
    final_file = "reproduce_shutdown.png"
    pressplot.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
