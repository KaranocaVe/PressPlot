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
    palette = pressplot.themes.CLEAN_MODERN_SCATTER_PALETTE
    dot_color = palette["dot_color"]
    line_color = palette["line_color"]
    text_color = palette["text_color"]
    stroke_color = palette["highlight_stroke"]

    fig, ax = plt.subplots(figsize=(12, 7))

    # 1. Generate Synthetic Data
    # Positive correlation between Public-sector workers (X) and Government effectiveness (Y)
    np.random.seed(101)
    n_points = 80

    # X: 0 to 100 (proxy)
    x = np.random.uniform(10, 90, n_points)

    # Y: correlated with X
    slope = 0.5
    intercept = 20
    noise = np.random.normal(0, 15, n_points)
    y = slope * x + intercept + noise

    # Sizes: Varying
    sizes = np.random.uniform(50, 400, n_points)

    # Plot background bubbles
    ax.scatter(x, y, s=sizes, color=dot_color, alpha=1.0, edgecolors='none')

    # 2. Trend Line
    # Dashed red line
    # Fit a line
    m, b = np.polyfit(x, y, 1)
    x_line = np.array([10, 95])
    y_line = m * x_line + b

    ax.plot(x_line, y_line, color=line_color, linewidth=4, linestyle='--', dashes=(4, 2))

    # 3. Specific Countries (Manual Placement to match image)
    # Chad: Low X, Low Y
    # Haiti: Mid-Low X, Low Y
    # US: High X, High Y (Large bubble with outline)
    # Britain: High X, High Y (On the line)
    # Australia: Very High X, High Y

    countries = [
        {"name": "Chad", "x": 15, "y": 25, "s": 80, "outline": True},
        {"name": "Haiti", "x": 35, "y": 20, "s": 100, "outline": True},
        {"name": "US", "x": 70, "y": 75, "s": 900, "outline": True},
        {"name": "Britain", "x": 85, "y": 68, "s": 150, "outline": True},
        {"name": "Australia", "x": 92, "y": 78, "s": 100, "outline": True},
    ]

    for c in countries:
        # Draw the dot
        edge = stroke_color if c["outline"] else 'none'
        lw = 1.5 if c["outline"] else 0

        # For US, Britain, Australia, the dot color is same salmon
        ax.scatter(c["x"], c["y"], s=c["s"], color=dot_color,
                   edgecolor=edge, linewidth=lw, zorder=10)

        # Label
        # Offset varies
        if c["name"] == "Chad":
            ax.text(c["x"] - 5, c["y"] - 2, c["name"], ha='right', va='top', fontsize=24, color=text_color)
        elif c["name"] == "Haiti":
            ax.text(c["x"], c["y"] - 8, c["name"], ha='center', va='top', fontsize=24, color=text_color)
        elif c["name"] == "US":
            ax.text(c["x"] + 5, c["y"] + 5, c["name"], ha='left', va='bottom', fontsize=24, color=text_color)
        elif c["name"] == "Britain":
            ax.text(c["x"], c["y"] - 8, c["name"], ha='center', va='top', fontsize=24, color=text_color)
        elif c["name"] == "Australia":
            ax.text(c["x"], c["y"] + 5, c["name"], ha='center', va='bottom', fontsize=24, color=text_color)

    # 4. Layout & Axes
    ax.axis('off')

    # Labels
    # "Government effectiveness ↑" (Top Right)
    ax.text(1.0, 1.05, "Government effectiveness ↑",
            transform=ax.transAxes, ha='right', va='bottom',
            fontsize=28, fontweight='bold', fontname="Arial", color=text_color)

    # "Public-sector workers per person →" (Bottom Left)
    ax.text(0.0, -0.05, "Public-sector workers per person →",
            transform=ax.transAxes, ha='left', va='top',
            fontsize=28, fontweight='bold', fontname="Arial", color=text_color)

    # Adjust limits
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)

    # Save
    final_file = "reproduce_scatter.png"
    pressplot.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
