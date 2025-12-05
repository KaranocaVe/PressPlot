import os
import sys

import geopandas as gpd
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import pressplot
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pressplot


def main():
    pressplot.load_theme("clean_modern")

    # Load World Data
    # We assume world.geojson is in the current directory or same directory as script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    # Check current dir first (where we downloaded it), then script dir
    if os.path.exists("world.geojson"):
        map_file = "world.geojson"
    elif os.path.exists(os.path.join(script_dir, "world.geojson")):
        map_file = os.path.join(script_dir, "world.geojson")
    else:
        print("Error: world.geojson not found. Please run the download command.")
        return

    world = gpd.read_file(map_file)

    # Filter out Antarctica for better view
    world = world[world.name != "Antarctica"]

    # Generate synthetic data for "Childhood obesity rates"
    # We'll just use random numbers seeded for reproducibility
    np.random.seed(42)
    world['obesity_rate'] = np.random.randint(0, 49, size=len(world))

    # Setup Figure
    fig, ax = plt.subplots(figsize=(14, 8))

    # Define Colormap and Norm
    # We use the discrete colormap from our theme
    cmap = plt.get_cmap("clean_modern_reds_discrete")

    # Define bins/bounds matching the reference image style
    # <10, 10-20, 20-30, 30-40, 40-50, >50
    bounds = [0, 10, 20, 30, 40, 50, 100]
    norm = mcolors.BoundaryNorm(bounds, cmap.N)

    # Plot
    world.plot(column='obesity_rate', ax=ax, cmap=cmap, norm=norm,
               edgecolor='white', linewidth=0.5)

    # Remove Axis and Ticks explicitly to avoid font warnings for negative coordinates
    ax.axis('off')
    ax.set_xticks([])
    ax.set_yticks([])

    # Title
    # Center aligned as per new reference
    ax.set_title("Childhood obesity rates", fontsize=32, fontweight='bold', loc='center', pad=40)

    # Add Horizontal Colorbar at the top
    # Create an axis for the colorbar
    # Centered below title.
    # [left, bottom, width, height]
    cbar_ax = fig.add_axes((0.35, 0.88, 0.3, 0.015))

    cb = plt.colorbar(plt.cm.ScalarMappable(norm=norm, cmap=cmap), cax=cbar_ax,
                      orientation='horizontal', ticks=[])  # No ticks

    # Remove outline of colorbar if needed, or keep it clean
    cb.outline.set_linewidth(0)

    # Add labels
    labels = ["<10", "10-20", "20-30", "30-40", "40-50", ">50"]
    for i, label in enumerate(labels):
        cbar_ax.text((i + 0.5) / len(labels), -0.5, label,
                     ha='center', va='top', transform=cbar_ax.transAxes, fontsize=12)

    # Save
    final_file = "reproduce_map.png"
    pressplot.save_clean_modern_style(fig, final_file, border_width=0)
    print(f"Saved {final_file}")


if __name__ == "__main__":
    main()
