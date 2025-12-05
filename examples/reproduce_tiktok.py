import os
import sys

import matplotlib.patches as patches
import matplotlib.pyplot as plt

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    plottheme.load_theme("clean_modern")

    # Colors
    palette = plottheme.themes.CLEAN_MODERN_TIKTOK_PALETTE
    c_red = palette["red"]
    c_pink = palette["pink"]
    c_grey = palette["grey"]
    c_border = palette["border"]

    fig, ax = plt.subplots(figsize=(12, 7))

    # Canvas setup
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.set_aspect('equal')
    ax.axis('off')

    # Data Layout (x, y, width, height, color, label)
    # Origin is bottom-left.

    rects = [
        # Left Column
        # Selfies (Bottom)
        {"x": 0, "y": 0, "w": 44, "h": 32, "c": c_red, "label": "Selfies"},
        # Lip-sync (Top)
        {"x": 0, "y": 32, "w": 44, "h": 68, "c": c_red, "label": "Lip-sync"},

        # Middle Column
        # Video Games (Bottom)
        {"x": 44, "y": 0, "w": 24, "h": 18, "c": c_pink, "label": "Video\nGames"},
        # Dance
        {"x": 44, "y": 18, "w": 24, "h": 18, "c": c_pink, "label": "Dance"},
        # Outfits
        {"x": 44, "y": 36, "w": 24, "h": 18, "c": c_pink, "label": "Outfits"},
        # Babies (Top)
        {"x": 44, "y": 54, "w": 24, "h": 46, "c": c_pink, "label": "Babies"},

        # Right Column
        # Other (Bottom)
        {"x": 68, "y": 0, "w": 32, "h": 88, "c": c_grey, "label": "Other"},
        # Cars (Top Left)
        {"x": 68, "y": 88, "w": 19, "h": 12, "c": c_pink, "label": "Cars"},
        # Pets (Top Right)
        {"x": 87, "y": 88, "w": 13, "h": 12, "c": c_pink, "label": "Pets"},
    ]

    # Draw Rectangles
    for r in rects:
        # Create rectangle
        rect = patches.Rectangle(
            (r["x"], r["y"]), r["w"], r["h"],
            linewidth=2, edgecolor=c_border, facecolor=r["c"]
        )
        ax.add_patch(rect)

        # Add Label
        # Top-left corner of the rectangle with padding
        pad_x = 1.5
        pad_y = 1.5

        # For "Other", it seems aligned to the top-left of its box too.

        label_x = r["x"] + pad_x
        label_y = r["y"] + r["h"] - pad_y

        ax.text(
            label_x, label_y, r["label"],
            ha='left', va='top',
            fontsize=22, fontweight='bold', color='black'
        )

    # Title
    # Centered above the chart
    ax.set_title("TikTok posts by category", fontsize=28, fontweight='bold', pad=20)

    # Save
    final_file = "reproduce_tiktok.png"
    plottheme.save_clean_modern_style(fig, final_file)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
