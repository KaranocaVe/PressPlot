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
    categories = np.arange(0, 16, 2)  # 0, 2, 4, ... 14
    # Male data (positive)
    male_data = [25, 12, 18, 10, 6, 3, 1, 1]  # Approx
    # Female data (negative for plotting)
    female_data = [-30, -20, -25, -5, -2, 0, 0, 0]  # Approx

    fig, ax = plt.subplots(figsize=(10, 8))

    # Plot Bars
    # Male (Red)
    ax.bar(categories, male_data, width=1.8, color='#E62A24', label='Male', align='center')
    # Female (Pink/Light Red)
    # Image shows female bars are lighter/transparent? Or just pink?
    # Let's use a lighter shade from our palette.
    pink_color = '#F7A493'
    ax.bar(categories, female_data, width=1.8, color=pink_color, label='Female', align='center')

    # Grid
    # Horizontal lines only.
    ax.grid(axis='y', color='#d4d4d4', linewidth=1.5)
    ax.grid(axis='x', visible=False)

    # Thick Zero Line (X-axis)
    ax.axhline(0, color='black', linewidth=3)

    # Labels
    # Y-axis on the right?
    # Matplotlib allows ax.yaxis.tick_right()
    ax.yaxis.tick_right()
    ax.yaxis.set_label_position("right")

    # Y-ticks: 30, 15, 0, 15, 30
    # We need to format negative labels as positive
    yticks = [-30, -15, 0, 15, 30]
    ax.set_yticks(yticks)
    ax.set_yticklabels(["30", "15", "0", "15", "30"], fontsize=18, fontweight='bold')

    # X-ticks: 0, 2, 4...
    ax.set_xticks(np.arange(0, 16, 2))
    ax.set_xticklabels(np.arange(0, 16, 2), fontsize=18, fontweight='bold')

    # Add "Drinks" label on the left of the zero line?
    # The image has "Drinks" on the left, "Male" above, "Female" below.
    ax.text(-2, 0.5, "Drinks", fontsize=20, fontweight='bold', ha='right', va='bottom')
    ax.text(-2, 8, "Male", fontsize=20, fontweight='bold', ha='right')
    ax.text(-2, -8, "Female", fontsize=20, fontweight='bold', ha='right')

    # Title
    # Left aligned at top
    # "What do you consider to be drinking in moderation?,"
    # "% responding"

    # We can use suptitle for the main title and ax.set_title for subtitle?
    # Or text.

    # Let's place title relative to axes
    ax.text(-2, 38, "What do you consider to be drinking in moderation?,",
            fontsize=26, fontweight='bold', ha='left')
    ax.text(-2, 34, "% responding",
            fontsize=22, fontweight='bold', ha='left')

    # Adjust limits
    ax.set_ylim(-35, 35)
    ax.set_xlim(-1, 16)

    # Remove Spines
    ax.spines['top'].set_visible(False)
    ax.spines['left'].set_visible(False)  # No left spine
    ax.spines['right'].set_visible(False)  # No right spine (ticks only)
    ax.spines['bottom'].set_visible(False)  # Zero line replaces bottom spine

    # Tick params
    ax.tick_params(axis='y', length=0)  # No ticks, just labels
    ax.tick_params(axis='x', length=0)

    final_file = "reproduce_drinking.png"
    pressplot.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
