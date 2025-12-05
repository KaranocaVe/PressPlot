import os
import sys

import matplotlib.pyplot as plt

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    plottheme.load_theme("clean_modern")

    # Colors
    blue_color = "#4A6FA5"  # Soft blue (Dems)
    red_color = "#E64B35"  # Soft red (Reps)
    grey_bar_color = "#D9D9D3"  # Beige/Grey for the track
    black_text = "#1B1919"

    fig, ax = plt.subplots(figsize=(10, 6))

    # Data
    # Row 1: Dems
    dems_actual = 11
    dems_est = 39
    dems_y = 2

    # Row 2: Reps
    reps_actual = 10
    reps_est = 41
    reps_y = 1

    # --- Plotting ---

    # 1. Grey Bars (Tracks)
    # Connect Actual to Estimated
    bar_height = 0.3

    # Dems Bar
    ax.barh(dems_y, dems_est - dems_actual, left=dems_actual, height=bar_height,
            color=grey_bar_color, edgecolor='none', zorder=1)

    # Reps Bar
    ax.barh(reps_y, reps_est - reps_actual, left=reps_actual, height=bar_height,
            color=grey_bar_color, edgecolor='none', zorder=1)

    # 2. Circles (Actual)
    # Dems (Blue)
    ax.scatter(dems_actual, dems_y, s=600, color=blue_color, zorder=3)
    # Reps (Red)
    ax.scatter(reps_actual, reps_y, s=600, color=red_color, zorder=3)

    # 3. Vertical Lines (Estimated)
    # Dems (Black line at 39)
    # Make it a thick vertical line segment covering the bar height
    ax.plot([dems_est, dems_est], [dems_y - bar_height / 2, dems_y + bar_height / 2],
            color='black', linewidth=6, solid_capstyle='butt', zorder=3)

    # Reps (Black line at 41)
    ax.plot([reps_est, reps_est], [reps_y - bar_height / 2, reps_y + bar_height / 2],
            color='black', linewidth=6, solid_capstyle='butt', zorder=3)

    # --- Labels ---

    # DEMS ROW
    # "Actual" (Blue) above circle
    ax.text(dems_actual, dems_y + 0.3, "Actual", color=blue_color,
            fontsize=20, ha='center', va='bottom')

    # "11" (Blue) left of circle
    ax.text(dems_actual - 2, dems_y, "11", color=blue_color,
            fontsize=24, fontweight='bold', ha='right', va='center')

    # "Dems" (Blue) Center of the bar?
    # Image shows "Dems" centered above the gap/bar.
    mid_dems = (dems_actual + dems_est) / 2
    ax.text(mid_dems, dems_y + 0.3, "Dems", color=blue_color,
            fontsize=24, fontweight='bold', ha='center', va='bottom')

    # "Estimated by Reps" (Black) above line
    ax.text(dems_est, dems_y + 0.3, "Estimated by Reps", color=black_text,
            fontsize=20, ha='center', va='bottom')

    # "39" (Black) right of line
    ax.text(dems_est + 2, dems_y, "39", color=black_text,
            fontsize=24, fontweight='bold', ha='left', va='center')

    # REPS ROW
    # "Actual" (Red) above circle
    ax.text(reps_actual, reps_y + 0.3, "Actual", color=red_color,
            fontsize=20, ha='center', va='bottom')

    # "10" (Red) left of circle
    ax.text(reps_actual - 2, reps_y, "10", color=red_color,
            fontsize=24, fontweight='bold', ha='right', va='center')

    # "Reps" (Red) Center
    mid_reps = (reps_actual + reps_est) / 2
    ax.text(mid_reps, reps_y + 0.3, "Reps", color=red_color,
            fontsize=24, fontweight='bold', ha='center', va='bottom')

    # "Estimated by Dems" (Black) above line
    ax.text(reps_est, reps_y + 0.3, "Estimated by Dems", color=black_text,
            fontsize=20, ha='center', va='bottom')

    # "41" (Black) right of line
    ax.text(reps_est + 2, reps_y, "41", color=black_text,
            fontsize=24, fontweight='bold', ha='left', va='center')

    # --- Titles ---
    # Main Title
    fig.text(0.5, 0.92, "Support for political violence",
             ha='center', va='top', fontsize=26, fontweight='bold', color=black_text)

    # Subtitle
    fig.text(0.5, 0.85, "100=max",
             ha='center', va='top', fontsize=20, fontweight='normal', color=black_text)

    # --- Axes Setup ---
    ax.set_xlim(0, 50)  # Based on data range, extend enough for labels
    ax.set_ylim(0.5, 2.8)

    # Remove everything
    ax.axis('off')

    # Save
    output_file = "reproduce_political_violence.png"
    plottheme.save_clean_modern_style(fig, output_file)
    print(f"Saved {output_file}")


if __name__ == "__main__":
    main()
