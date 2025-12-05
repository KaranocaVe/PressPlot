import os
import sys

import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import make_interp_spline

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def generate_smooth_curve(x_points, y_points, n_points=100, noise_level=0.5):
    """Generates a smooth curve passing through points with added noise."""
    spline = make_interp_spline(x_points, y_points, k=3)
    x_new = np.linspace(min(x_points), max(x_points), n_points)
    y_new = spline(x_new)

    # Add some jaggedness to mimic the original chart
    noise = np.random.normal(0, noise_level, size=n_points)
    # Smooth the noise a bit so it's not too jittery
    noise = np.convolve(noise, np.ones(3) / 3, mode='same')

    return x_new, y_new + noise


def main():
    plottheme.load_theme("clean_modern")

    # Colors
    # Using the palette from themes.py or approximating from image
    # Red for Boys, Pink for Girls
    red_color = "#E62A24"
    pink_color = "#F4A598"  # Lighter pink/salmon

    fig = plt.figure(figsize=(12, 7))

    # Layout Strategy: Manual placement to ensure control
    # Left Chart: [0.05, 0.15, 0.40, 0.55]
    # Right Chart: [0.55, 0.15, 0.40, 0.55]
    # Header area: Top 30%

    ax1 = fig.add_axes([0.05, 0.2, 0.42, 0.50])  # Left
    ax2 = fig.add_axes([0.53, 0.2, 0.42, 0.50])  # Right

    # Shared settings
    axes = [ax1, ax2]
    x_range = np.linspace(0, 100, 100)

    # --- Data Generation ---

    # Left Chart: Beginning of 1st year
    # Boys: Slight U shape, generally flat around 48
    boys_left_x = [0, 20, 50, 80, 100]
    boys_left_y = [52, 45, 44, 48, 52]
    x_l, y_boys_l = generate_smooth_curve(boys_left_x, boys_left_y)

    # Girls: Slight inverted U shape, generally flat around 52
    girls_left_x = [0, 20, 50, 80, 100]
    girls_left_y = [38, 48, 50, 48, 38]
    _, y_girls_l = generate_smooth_curve(girls_left_x, girls_left_y)

    # Right Chart: Beginning of 2nd year
    # Boys: Starts mid, dips, then shoots up
    boys_right_x = [0, 10, 40, 70, 90, 100]
    boys_right_y = [55, 42, 40, 55, 70, 85]
    x_r, y_boys_r = generate_smooth_curve(boys_right_x, boys_right_y)

    # Girls: Starts mid, goes up, then drops hard
    girls_right_x = [0, 10, 40, 70, 90, 100]
    girls_right_y = [45, 55, 58, 50, 35, 15]
    _, y_girls_r = generate_smooth_curve(girls_right_x, girls_right_y)

    # --- Plotting ---

    # Left
    ax1.plot(x_l, y_girls_l, color=pink_color, linewidth=6, solid_capstyle='round')
    ax1.plot(x_l, y_boys_l, color=red_color, linewidth=6, solid_capstyle='round')

    # Right
    ax2.plot(x_r, y_girls_r, color=pink_color, linewidth=6, solid_capstyle='round')
    ax2.plot(x_r, y_boys_r, color=red_color, linewidth=6, solid_capstyle='round')

    # --- Styling ---

    for ax in axes:
        # Limits
        ax.set_ylim(10, 90)
        ax.set_xlim(0, 100)

        # Grid
        # Only horizontal lines at 20, 50, 80
        ax.set_yticks([20, 50, 80])
        ax.grid(axis='y', color='#d4d4d4', linewidth=1.5, zorder=0)
        ax.grid(axis='x', visible=False)

        # Spines
        ax.spines['top'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(True)
        ax.spines['bottom'].set_linewidth(2)
        ax.spines['bottom'].set_color('black')

        # X Ticks
        ax.set_xticks([])  # No x numbers
        ax.set_xlabel("Score percentile", fontsize=22, fontweight='normal', labelpad=15, color='black')

    # Y Axis Labels
    # Left chart: None
    ax1.set_yticklabels([])
    ax1.tick_params(axis='y', length=0)

    # Right chart: Labels on the right
    ax2.yaxis.tick_right()
    ax2.set_yticklabels(["20", "50", "80"], fontsize=22, fontweight='normal')
    ax2.tick_params(axis='y', length=0, pad=10)

    # --- Text & Titles ---

    # Subplot Titles
    # Positioned manually above the plots
    fig.text(0.26, 0.75, "Beginning of 1st year", ha='center', va='bottom',
             fontsize=24, fontweight='bold', color='#1B1919')

    fig.text(0.74, 0.75, "Beginning of 2nd year", ha='center', va='bottom',
             fontsize=24, fontweight='bold', color='#1B1919')

    # Main Title
    fig.text(0.05, 0.88, "Performance of French children in maths, % of children",
             ha='left', va='top', fontsize=26, fontweight='bold', color='#1B1919')

    # Annotations on Right Chart
    # "Boys" near the end of red line
    ax2.text(85, 75, "Boys", fontsize=22, fontweight='normal', ha='right', va='center', color='black')

    # "Girls" near the end of pink line
    ax2.text(85, 25, "Girls", fontsize=22, fontweight='normal', ha='right', va='center', color='black')

    # Save
    final_file = "reproduce_french_math.png"
    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
