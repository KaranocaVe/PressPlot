import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Add parent directory to path to import pressplot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pressplot


def smooth_line(x, y, num_points=300):
    """Interpolates points to create a smooth curve."""
    x_new = np.linspace(min(x), max(x), num_points)
    spl = make_interp_spline(x, y, k=3)  # Cubic spline
    y_smooth = spl(x_new)
    return x_new, y_smooth


def main():
    pressplot.load_theme("clean_modern")

    # Data (Approximate from image)
    years = np.array([2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025])

    # Rankings (1 is high, 10 is low) -> We will invert Y axis later or map 1->10, 10->1
    # Let's use raw rank values and invert axis
    germany_rank = np.array([4, 3, 3, 3, 5, 5, 4, 3, 3, 1, 4])  # Black line
    us_rank = np.array([2, 4, 5, 5, 6, 9, 7, 6, 7, 7, 12])  # Red line (drops off)

    # Create figure
    fig, ax = plt.subplots(figsize=(10, 6))

    # Disable default grid because we want dots
    ax.grid(False)

    # Draw Dot Grid
    # Y axis: 1 to 10
    y_grid = np.arange(1, 11)
    # X axis: 2015 to 2025
    x_grid = years
    pressplot.draw_dot_grid(ax, x_grid, y_grid, color='#B6B6A9', size=25)

    # Plot Smooth Lines
    # We need to handle the "step" nature or "bump" nature. 
    # The image shows smooth transitions but holding levels.
    # Let's just use cubic spline for now.

    x_smooth_g, y_smooth_g = smooth_line(years, germany_rank)
    x_smooth_u, y_smooth_u = smooth_line(years, us_rank)

    # Plot Background Lines (Faint grey lines for other countries?)
    # The image shows faint lines in the background.
    # We can simulate this with random walks or just omit for now to focus on the main style.
    # Let's add a few dummy faint lines for effect
    np.random.seed(42)
    for _ in range(5):
        start_rank = np.random.randint(1, 11)
        ranks = [start_rank]
        for _ in range(len(years) - 1):
            change = np.random.choice([-1, 0, 1])
            new_rank = np.clip(ranks[-1] + change, 1, 10)
            ranks.append(new_rank)
        x_s, y_s = smooth_line(years, np.array(ranks))
        ax.plot(x_s, y_s, color='#d4d4d4', linewidth=1.5, alpha=0.5, zorder=1)

    # Plot Main Lines
    # Germany (Black)
    ax.plot(x_smooth_g, y_smooth_g, color='#000000', linewidth=4, zorder=3)
    # Points for Germany
    ax.scatter(years, germany_rank, color='#000000', s=60, zorder=4)

    # US (Red)
    red_color = '#F04E3E'  # Slightly brighter red from image
    ax.plot(x_smooth_u, y_smooth_u, color=red_color, linewidth=4, zorder=3)
    # Points for US
    ax.scatter(years, us_rank, color=red_color, s=60, zorder=4)

    # Labels
    ax.text(2025.2, germany_rank[-1], "Germany", color='black', fontsize=20, fontweight='bold', va='center')
    ax.text(2025.2, us_rank[-1], "United States", color=red_color, fontsize=20, fontweight='bold', va='center')

    # Title
    # Centered title
    ax.set_title("Passport strength", fontsize=26, fontweight='bold', pad=20, loc='center')

    # Axis settings
    ax.set_ylim(10.5, 0.5)  # Invert Y axis: 1 at top, 10 at bottom
    ax.set_yticks([1, 5, 10])
    ax.set_yticklabels(["1st", "5th", "10th"], fontsize=18, fontweight='bold')

    ax.set_xlim(2014.8, 2025.2)
    ax.set_xticks([2015, 2020, 2025])
    ax.set_xticklabels(["2015", "2020", "2025"], fontsize=18, fontweight='bold')

    # Remove spines
    ax.spines['bottom'].set_visible(False)  # No bottom line in this chart
    ax.spines['left'].set_visible(False)

    # Remove ticks
    ax.tick_params(axis='both', length=0)  # No tick marks

    # Align Y labels
    # In the image, 1st, 5th, 10th are on the left, aligned right?
    # They seem to float.

    final_file = "reproduce_passport.png"
    pressplot.save_clean_modern_style(fig, final_file,
                                      border_width=0)  # No extra border needed for this specific look? Or maybe yes.
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
