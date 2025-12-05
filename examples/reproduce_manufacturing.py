import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme
from scipy.interpolate import make_interp_spline


def smooth_line(x, y, points=300):
    x_new = np.linspace(min(x), max(x), points)
    spl = make_interp_spline(x, y, k=3)
    y_smooth = spl(x_new)
    return x_new, y_smooth


def main():
    plottheme.load_theme("clean_modern")

    # Colors
    colors = plottheme.themes.CLEAN_MODERN_MANUFACTURING_PALETTE
    blue_germany = colors[0]
    pink_britain = colors[1]
    grey_us = colors[2]
    red_china = colors[3]

    fig, ax = plt.subplots(figsize=(12, 7))

    # Data Generation (Approximation)
    # X-axis: 0 to 100 (GDP per person proxy)

    # Germany: High start, curve up, then steady decline
    x_ger = np.array([15, 25, 35, 50, 70, 85])
    y_ger = np.array([30, 33, 32, 25, 18, 15])
    x_ger_s, y_ger_s = smooth_line(x_ger, y_ger)

    # Britain: High start (lower than Ger), sharp decline
    x_uk = np.array([10, 20, 30, 40, 55, 75])
    y_uk = np.array([28, 32, 28, 18, 10, 8])
    x_uk_s, y_uk_s = smooth_line(x_uk, y_uk)

    # US: Medium start, gentle curve, flatten
    x_us = np.array([20, 30, 40, 60, 80, 100])
    y_us = np.array([15, 20, 18, 12, 8, 9])
    x_us_s, y_us_s = smooth_line(x_us, y_us)

    # China: Low start, sharp rise, dip, rise?
    # Image: Starts very low, goes up steeply to a peak, then stops/fades?
    # Actually, the red line is short.
    x_cn = np.array([5, 10, 15, 20, 30])
    y_cn = np.array([5, 15, 14, 18, 22])
    x_cn_s, y_cn_s = smooth_line(x_cn, y_cn)

    # Plotting
    lw = 6  # Thick lines

    ax.plot(x_ger_s, y_ger_s, color=blue_germany, linewidth=lw)
    ax.plot(x_uk_s, y_uk_s, color=pink_britain, linewidth=lw)
    ax.plot(x_us_s, y_us_s, color=grey_us, linewidth=lw)
    ax.plot(x_cn_s, y_cn_s, color=red_china, linewidth=lw)

    # Grid
    ax.grid(axis='y', color='#d4d4d4', linewidth=2)
    ax.grid(axis='x', visible=False)

    # Remove spines
    ax.spines['left'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['top'].set_visible(False)
    ax.spines['bottom'].set_visible(False)

    # Remove ticks and labels
    ax.set_xticks([])
    # We need y-ticks to generate grid lines, but we hide the labels and ticks themselves
    ax.set_yticks([0, 10, 20, 30, 40])
    ax.tick_params(axis='y', length=0, labelleft=False)

    # Grid (Make sure it's behind the plot elements)
    ax.set_axisbelow(True)
    ax.grid(axis='y', color='#d4d4d4', linewidth=2, alpha=1.0)

    # Title (Right Aligned with Arrow)
    # Using figure text or axes text relative to axes
    # Explicitly using Arial for arrows to avoid glyph missing warning
    ax.text(1.0, 1.05, "Manufacturing as % of total employment ↑",
            transform=ax.transAxes, ha='right', fontsize=24, fontweight='bold', fontname="Arial")

    # X Label (Left Aligned with Arrow)
    ax.text(0.0, -0.05, "GDP per person →",
            transform=ax.transAxes, ha='left', fontsize=24, fontweight='bold', fontname="Arial")

    # Line Labels
    # Germany (Blue) - Above the line
    ax.text(55, 26, "Germany", color=blue_germany, fontsize=24, fontweight='bold')

    # Britain (Pink) - Inside the curve
    # "Britain" text is reddish-orange. The line is pink/salmon.
    ax.text(22, 25, "Britain", color="#E62A24", fontsize=24, fontweight='bold')

    # US (Grey) - At the end
    ax.text(90, 10, "US", color='#555555', fontsize=24, fontweight='bold')

    # China (Red) - Below the curve
    ax.text(10, 8, "China", color=red_china, fontsize=24, fontweight='bold')

    # Adjust limits
    ax.set_xlim(0, 110)
    ax.set_ylim(0, 40)

    # Save
    final_file = "reproduce_manufacturing.png"
    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
