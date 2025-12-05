import os
import sys

import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    plottheme.load_theme("clean_modern")

    fig, ax = plt.subplots(figsize=(12, 7))

    # 1. Generate Synthetic Data
    np.random.seed(42)
    n_points = 1500

    # X: Temperature Percentile (0 to 100)
    x = np.random.uniform(0, 100, n_points)

    # Y: Risk of death (Same curve as before)
    y = []
    for val in x:
        if val < 35:
            base = 0.2
            noise = np.random.normal(0, 0.1)
            y.append(max(0, base + noise))
        else:
            norm_x = (val - 35) / 65
            base = 0.2 + 1.2 * (norm_x ** 2)
            noise = np.random.normal(0, 0.1 + 0.2 * norm_x)
            y.append(max(0, base + noise))

    y = np.array(y)
    sizes = np.random.uniform(30, 180, n_points)

    # 2. Discrete Color Stacking Logic
    # We define discrete colors and assign them based on X with some probabilistic overlap

    c_dark_blue = "#2A4B7C"
    c_mid_blue = "#7EA0C6"
    c_pale_pink = "#F4C9C4"  # Light pink/beige for the middle-right
    c_red = "#D92E27"

    # Assign colors
    point_colors = []

    for val in x:
        # Random component for overlap
        r = np.random.random()

        if val < 25:
            # Mostly Dark Blue, some Mid Blue
            if r < 0.8:
                color = c_dark_blue
            else:
                color = c_mid_blue
        elif val < 45:
            # Mix of Dark Blue and Mid Blue, slightly more Mid
            if r < 0.3:
                color = c_dark_blue
            elif r < 0.9:
                color = c_mid_blue
            else:
                color = c_pale_pink
        elif val < 70:
            # Transition from Mid Blue to Pale Pink
            if r < 0.4:
                color = c_mid_blue
            elif r < 0.9:
                color = c_pale_pink
            else:
                color = c_red
        else:
            # Mostly Red, some Pale Pink
            if r < 0.2:
                color = c_pale_pink
            else:
                color = c_red

        point_colors.append(color)

    # Shuffle the plotting order so colors mix naturally (not one on top of another)
    indices = np.arange(n_points)
    np.random.shuffle(indices)

    x_shuffled = x[indices]
    y_shuffled = y[indices]
    s_shuffled = sizes[indices]
    c_shuffled = np.array(point_colors)[indices]

    # Plot background bubbles
    # No cmap, direct color list
    ax.scatter(x_shuffled, y_shuffled, s=s_shuffled, c=c_shuffled, alpha=0.75, edgecolors='none')

    # 3. Highlight Specific Cities
    # Same locations and colors as before
    cities = [
        {"name": "London", "x": 38, "y": 0.45, "color": c_dark_blue, "s": 1100},
        {"name": "Paris", "x": 55, "y": 0.65, "color": c_mid_blue, "s": 1200},
        {"name": "Milan", "x": 72, "y": 1.25, "color": c_red, "s": 800},
        {"name": "Madrid", "x": 86, "y": 0.60, "color": c_red, "s": 900},
    ]

    for city in cities:
        ax.scatter(city["x"], city["y"], s=city["s"], color=city["color"],
                   edgecolor='#1B1919', linewidth=1.5, zorder=10)

        font_props = {'family': 'serif', 'name': 'Times New Roman', 'size': 24, 'weight': 'normal'}

        if city["name"] == "London":
            ax.text(city["x"] - 3, city["y"] + 0.15, city["name"],
                    ha='right', **font_props, color='#1B1919')
        elif city["name"] == "Paris":
            ax.text(city["x"] - 3, city["y"] + 0.15, city["name"],
                    ha='right', **font_props, color='#1B1919')
        elif city["name"] == "Milan":
            ax.text(city["x"] - 3, city["y"] + 0.10, city["name"],
                    ha='right', **font_props, color='#1B1919')
        elif city["name"] == "Madrid":
            ax.text(city["x"], city["y"] - 0.25, city["name"],
                    ha='center', **font_props, color='#1B1919')

    # 4. Layout & Axes
    ax.axis('off')

    ax.text(1.0, 1.05, "Relative risk of death ↑",
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=32, fontweight='bold', fontname="Arial", color='#1B1919')

    ax.text(0.0, -0.05, "→ 99th temperature percentile",
            transform=ax.transAxes, ha='left', va='top',
            fontsize=32, fontweight='bold', fontname="Arial", color='#333333')

    ax.set_xlim(-5, 105)
    ax.set_ylim(-0.1, 1.5)

    final_file = "reproduce_bubble.png"
    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
