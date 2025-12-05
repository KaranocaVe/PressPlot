import os
import sys

import cartopy.crs as ccrs
import cartopy.io.shapereader as shpreader
import matplotlib.path as mpath
import matplotlib.pyplot as plt
import numpy as np

# Add parent directory to path to import plottheme
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import plottheme


def main():
    # Load theme
    plottheme.load_theme("clean_modern")

    # Colors
    bg_color = "#F1F0EA"  # Page background
    ocean_color = "#F7F7F7"  # Very light grey/white for ocean
    land_color = "#E6E6E6"  # Light grey for land
    greenland_color = "#E62A24"  # Red
    grid_color = "#D4D4D4"  # Grid line color
    border_color = "#888888"  # Globe border

    # 1. Setup Projection
    central_lon = -40
    central_lat = 72
    projection = ccrs.Orthographic(central_longitude=central_lon, central_latitude=central_lat)

    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(1, 1, 1, projection=projection)

    # 2. Globe Boundary & Ocean
    # Create a circular path for the globe
    theta = np.linspace(0, 2 * np.pi, 100)
    center, radius = [0.5, 0.5], 0.5
    verts = np.vstack([np.sin(theta), np.cos(theta)]).T
    circle = mpath.Path(verts * radius + center)

    ax.set_boundary(circle, transform=ax.transAxes)

    # Fill the background (Ocean)
    # When using set_boundary, the axes background patch is clipped to the circle.
    ax.patch.set_facecolor(ocean_color)

    # 3. Load Data
    shpfilename = shpreader.natural_earth(resolution='110m',
                                          category='cultural',
                                          name='admin_0_countries')
    reader = shpreader.Reader(shpfilename)
    countries = reader.records()

    # 4. Plot Countries
    for country in countries:
        name = country.attributes.get('NAME', '')

        # Geometry
        geom = country.geometry

        if name == 'Greenland':
            ax.add_geometries([geom], ccrs.PlateCarree(),
                              facecolor=greenland_color,
                              edgecolor='none',
                              zorder=3)
        else:
            ax.add_geometries([geom], ccrs.PlateCarree(),
                              facecolor=land_color,
                              edgecolor='none',
                              zorder=2)

    # 5. Gridlines
    gl = ax.gridlines(color=grid_color, linestyle='-', linewidth=1.5, alpha=0.6, zorder=4)
    gl.xlocator = plt.FixedLocator(np.arange(-180, 181, 30))
    gl.ylocator = plt.FixedLocator(np.arange(-90, 91, 30))

    # 6. Aesthetics
    # Add a thin border around the globe
    # We can do this by adding a patch or using the spine?
    # In Cartopy with set_boundary, the spine is the boundary.
    ax.spines['geo'].set_edgecolor(border_color)
    ax.spines['geo'].set_linewidth(1.0)
    ax.spines['geo'].set_visible(True)

    # Set figure background
    fig.patch.set_facecolor(bg_color)

    # Save using the theme function which handles border addition
    output_file = "reproduce_greenland.png"
    plottheme.save_clean_modern_style(fig, output_file,
                                      border_color=bg_color,
                                      border_width=50,
                                      dpi=300,
                                      bbox_inches='tight',
                                      facecolor=bg_color)
    print(f"Saved {output_file}")


if __name__ == "__main__":
    main()
