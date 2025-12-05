import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import pressplot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pressplot


def main():
    pressplot.load_theme("clean_modern")

    # Colors
    palette = pressplot.themes.CLEAN_MODERN_TARIFF_PALETTE
    c_2024 = palette["2024_rate"]
    c_increase = palette["increase"]
    text_color = palette["text_color"]

    fig, ax = plt.subplots(figsize=(12, 6))

    # Data
    countries = ["Britain", "France", "Germany", "Mexico", "Switzerland", "India", "China"]
    # Values roughly estimated from image
    val_2024 = [2.0, 2.5, 3.0, 0.5, 1.0, 3.5, 12.0]
    val_increase = [9.0, 13.0, 15.0, 18.5, 24.0, 33.0, 34.0]

    y_pos = np.arange(len(countries))

    # Horizontal Stacked Bar Chart
    # 2024 rate (Base)
    bars1 = ax.barh(y_pos, val_2024, color=c_2024, height=0.65, align='center', zorder=3)

    # Increase (Stacked on top)
    bars2 = ax.barh(y_pos, val_increase, left=val_2024, color=c_increase, height=0.65, align='center', zorder=3)

    # White separators between segments
    for i in range(len(countries)):
        ax.plot([val_2024[i], val_2024[i]], [y_pos[i] - 0.325, y_pos[i] + 0.325], color='white', linewidth=1, zorder=4)

    # Grid
    ax.grid(axis='x', color='#d4d4d4', linewidth=1.5, zorder=0)
    ax.grid(axis='y', visible=False)

    # Vertical Line at 0
    ax.axvline(0, color='black', linewidth=2.5, zorder=5)

    # X-Axis Config
    ax.set_xlim(0, 50)
    ax.xaxis.tick_top()  # Ticks at top
    ax.tick_params(axis='x', labeltop=True, labelbottom=False)
    ax.set_xticks([0, 10, 20, 30, 40, 50])
    ax.set_xticklabels(["0", "10", "20", "30", "40", "50"], fontsize=24, fontweight='normal')

    # Y-Axis Config
    ax.set_yticks(y_pos)
    ax.set_yticklabels(countries, fontsize=24, fontweight='normal')

    # IMPORTANT: Force labels to the LEFT and hide ticks
    # Theme defaults to labelright=True, which causes overlaps with bars.
    ax.tick_params(axis='y', length=0, labelleft=True, labelright=False, pad=10)

    # Remove spines
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    # Title & Subtitle
    # Use fig.text relative to figure coordinates
    # Increased top margin to avoid collision with top x-ticks

    # Main Title
    fig.text(0.05, 0.95, "United States, effective tariff rate, %",
             fontsize=28, fontweight='bold', ha='left', va='top', color=text_color)

    # Subtitle
    fig.text(0.05, 0.88, "Weighted by 2024 imports",
             fontsize=24, fontweight='normal', ha='left', va='top', color=text_color)

    # Legend (Custom)
    # Bottom right corner
    # Square patches

    # 2024 rate
    import matplotlib.patches as patches
    fig.patches.extend([
        patches.Rectangle((0.70, 0.20), 0.025, 0.04, fill=True, color=c_2024, transform=fig.transFigure, zorder=10),
        patches.Rectangle((0.70, 0.13), 0.025, 0.04, fill=True, color=c_increase, transform=fig.transFigure, zorder=10)
    ])

    fig.text(0.735, 0.20, "2024 rate", fontsize=22, va='bottom', ha='left')
    fig.text(0.735, 0.13, "Increase in 2025", fontsize=22, va='bottom', ha='left')

    # Adjust margins
    # Increased left to 0.30 for long names like "Switzerland"
    # Decreased top to 0.70 to push plot down significantly, avoiding title overlap
    fig.subplots_adjust(left=0.30, right=0.95, top=0.70, bottom=0.1)

    # Save
    final_file = "reproduce_tariff.png"
    pressplot.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
