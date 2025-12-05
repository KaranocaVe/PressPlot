import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    # 1. Load the new theme (fonts are auto-registered)
    plottheme.load_theme("clean_modern")

    # Image Size: 12.8 x 7.2 inches (matches 1280x720 at 100 DPI)
    FIG_W = 12.8
    FIG_H = 7.2

    # Line Widths (Points)
    # Analysis suggested ~8px on 1280px width. 
    # 8px / 100dpi * 72pt/inch = 5.76pt. Let's use 5.0 for main lines.
    MAIN_LINE_WIDTH = 5.0
    GREY_LINE_WIDTH = 4.0

    # 2. Data
    years = np.arange(2014, 2026)
    sydney_vals = [36.2, 37.4, 36.5, 38.6, 36.2, 34.2, 29.6, 29.0, 31.8, 36.2, 37.0, 37.8]
    perth_vals = [25.0, 24.5, 22.0, 19.0, 18.2, 18.0, 17.0, 21.5, 22.0, 26.5, 27.8, 29.0]
    line_a = [31.0, 30.8, 30.5, 25.5, 25.8, 26.0, 25.0, 25.2, 28.5, 29.0, 28.0, 28.5]
    line_b = [26.5, 27.5, 27.0, 27.5, 27.6, 26.5, 25.0, 25.2, 29.0, 31.5, 30.5, 31.5]
    line_c = [24.5, 26.5, 25.5, 27.0, 27.0, 27.5, 24.5, 23.0, 25.0, 27.0, 28.0, 29.2]
    line_d = [23.5, 22.5, 21.5, 23.0, 22.5, 22.8, 23.2, 22.5, 24.0, 25.5, 25.2, 25.2]

    fig = plt.figure(figsize=(FIG_W, FIG_H))

    # Manual Axes Positioning from Analysis
    # ax.set_position([0.0359, 0.1486, 0.9273, 0.7653])
    # Left=46px, Right=1233px => Width=1187px => 1187/1280 = 0.9273
    # Bottom=613px (from top) => 720-613=107px from bottom => 107/720 = 0.1486
    # Top=62px (from top) => Height=551px => 551/720 = 0.7653

    # We need to be careful: Matplotlib axis position includes the area for data plotting (inner box).
    # Labels and titles are outside.
    # Adjusted to add more margin around the plot (User feedback: "贴上了" -> too tight)
    # Left: 0.05 (5%), Bottom: 0.15 (15%), Width: 0.90 (90%), Height: 0.73 (73%) -> Top at 0.88
    # Reverting to this "Balanced" layout because we will add an external border.
    ax = fig.add_axes((0.05, 0.15, 0.90, 0.73))
    # ax.set_position((0.08, 0.16, 0.84, 0.68)) # Previous "Extra Margin" attempt

    theme = plottheme.get_theme("clean_modern")
    palette = theme.palette
    red = palette[0]
    grey = palette[1]
    pink = palette[2]

    # Plot Lines
    grey_width = GREY_LINE_WIDTH
    main_width = MAIN_LINE_WIDTH

    ax.plot(years, line_a, color=grey, linewidth=grey_width, solid_capstyle='round')
    ax.plot(years, line_b, color=grey, linewidth=grey_width, solid_capstyle='round')
    ax.plot(years, line_c, color=grey, linewidth=grey_width, solid_capstyle='round')
    ax.plot(years, line_d, color=grey, linewidth=grey_width, solid_capstyle='round')

    ax.plot(years, sydney_vals, color=red, linewidth=main_width, solid_capstyle='round')
    ax.plot(years, perth_vals, color=pink, linewidth=main_width, solid_capstyle='round')

    # Title
    # Position: Top Left of the FIGURE, not Axes.
    # Analysis said Title x ~ 46px (same as plot left).
    # Matplotlib suptitle or text in figure coords.
    # Let's use ax.set_title but with coordinates relative to axes to align perfectly with left spine.
    # x=0 is left spine.
    # y=1 is top spine.
    # We need to lift it up. 
    # Analysis: Plot Top=62px. Title Top=?? Title detected above plot.
    # Let's place title slightly above the top spine.
    ax.set_title("Australian cities, one-bedroom rent as % of salary",
                 loc='left', x=0.0, y=1.02,  # Align with left spine (0.0), slightly above (1.02)
                 fontsize=24, fontweight='bold', pad=15)

    # Annotations
    font_size_label = 22  # Increased slightly
    font_size_tick = 20

    ax.text(2022.2, 36.5, "Sydney", color=red, fontsize=font_size_label, fontweight='bold', va='center')
    ax.text(2021.5, 20.5, "Perth", color=pink, fontsize=font_size_label, fontweight='bold', va='center')
    ax.text(2016.8, 30.5, "Other", color='#555555', fontsize=font_size_label, fontweight='bold', va='center')

    # Axes Config
    ax.set_xlim(2013.5, 2025.5)
    ax.set_xticks([2014, 2016, 2018, 2020, 2022, 2024, 2025])
    ax.set_xticklabels(["2014", "16", "18", "20", "22", "24", "25"], fontsize=font_size_tick, fontweight='bold')

    # Y-Axis
    ax.set_ylim(16, 41)
    ax.set_yticks([20, 25, 30, 35, 40])
    ax.tick_params(axis='y', labelsize=font_size_tick, pad=10)  # Add padding to labels
    for label in ax.get_yticklabels():
        label.set_fontweight('bold')

    # Move Y-axis labels to the right
    ax.yaxis.set_label_position("right")
    ax.yaxis.tick_right()
    ax.set_axisbelow(True)

    # Bottom Spine
    ax.spines['bottom'].set_color('#000000')
    ax.spines['bottom'].set_linewidth(2.5)  # Thicker

    # Tick Params - length
    ax.tick_params(axis='x', which='major', length=8, width=2, color='black')
    ax.tick_params(axis='y', length=0)  # No Y ticks, just labels

    final_file = "replicate_clean_modern_packaged.png"

    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Plot saved to {final_file}")


if __name__ == "__main__":
    main()
