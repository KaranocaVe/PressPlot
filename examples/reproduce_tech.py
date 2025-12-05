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
    palette = plottheme.themes.CLEAN_MODERN_TECH_PALETTE
    red_color = palette["highlight_red"]
    light_red = palette["light_red"]  # Maybe use this for lines? Or just same red with opacity?
    # Actually lines look slightly lighter in image, but it might just be anti-aliasing.
    # Let's use the same red for strong visual impact.
    grey_color = palette["grey_dot"]
    text_color = palette["text_color"]

    fig, ax = plt.subplots(figsize=(12, 7))

    # Categories
    categories = ["Space", "AI", "Semi-conductors", "Quantum", "Biotech"]
    x_pos = np.arange(len(categories))

    # Data (Approximated from image)
    # Top 3 Countries (Red Lines)
    # Line 1 (Top): US/China?
    line1 = [85, 82, 70, 78, 80]
    # Line 2 (Mid): 
    line2 = [50, 52, 55, 70, 50]
    # Line 3 (Bottom of top):
    line3 = [35, 40, 20, 75, 80]

    # Other Countries (Grey Dots)
    # Random clusters at the bottom (0-25)
    np.random.seed(42)
    for i in range(len(categories)):
        # Generate ~10-15 points per category
        n_others = 15
        # Y values clustered low
        y_others = np.random.uniform(0, 20, n_others)
        # X values with slight jitter for visual density
        x_others = np.random.normal(i, 0.02, n_others)

        ax.scatter(x_others, y_others, color=grey_color, s=100, alpha=0.3, edgecolors='none', zorder=2)

    # Plot Top Lines
    # Use zorder to put them on top of grid and grey dots
    lw = 4
    ms = 200  # Markersize area

    # Line 1
    ax.plot(x_pos, line1, color=light_red, linewidth=lw, zorder=3)
    ax.scatter(x_pos, line1, color=red_color, s=ms, zorder=4)

    # Line 2
    ax.plot(x_pos, line2, color=light_red, linewidth=lw, zorder=3)
    ax.scatter(x_pos, line2, color=red_color, s=ms, zorder=4)

    # Line 3
    ax.plot(x_pos, line3, color=light_red, linewidth=lw, zorder=3)
    ax.scatter(x_pos, line3, color=red_color, s=ms, zorder=4)

    # Grid
    ax.grid(axis='y', color='#d4d4d4', linewidth=1.5, zorder=0)
    # Vertical grid lines aligned with ticks
    ax.grid(axis='x', color='#d4d4d4', linewidth=1.5, zorder=0)

    # Axes Config
    ax.set_ylim(-5, 105)
    ax.set_yticks([0, 25, 50, 75, 100])
    # Move y-axis to right? No, image has labels on right.
    # Wait, image has "0, 25, 50, 75" on the RIGHT.
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")
    ax.set_yticklabels([0, 25, 50, 75, 100], fontsize=24, fontweight='normal')

    ax.set_xticks(x_pos)
    ax.set_xticklabels(categories, fontsize=24, fontweight='bold')

    # Spines
    # Bottom spine thick black
    ax.spines['bottom'].set_visible(True)
    ax.spines['bottom'].set_linewidth(2.5)
    ax.spines['bottom'].set_color('black')

    # Others hidden
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)

    # Tick params
    ax.tick_params(axis='x', length=0, pad=15)
    ax.tick_params(axis='y', length=0, pad=10)

    # Annotations
    # "Most developed=100" above 100 line on right
    ax.text(1.0, 1.02, "Most developed=100", transform=ax.transAxes,
            ha='right', va='bottom', fontsize=24, color=text_color)

    # "Top three countries" label
    # In the Space/AI gap, around y=65
    ax.text(0.5, 65, "Top three\ncountries", fontsize=24, fontweight='bold',
            color=red_color, ha='center', va='center',
            bbox=dict(facecolor='#F1F0EA', edgecolor='none', alpha=0.8, pad=5))

    # "Other" label
    # Near Quantum/Biotech, around y=15
    ax.text(3.5, 15, "Other", fontsize=24, fontweight='bold',
            color='#777777', ha='center', va='center')

    # Title
    fig.text(0.05, 0.95, "Critical technologies index by sector",
             fontsize=28, fontweight='bold', ha='left', va='top', color=text_color)

    # Adjust margins
    fig.subplots_adjust(left=0.05, right=0.90, top=0.85, bottom=0.1)

    # Save
    final_file = "reproduce_tech.png"
    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
