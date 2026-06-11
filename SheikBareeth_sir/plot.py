import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create data
lon = np.linspace(-180, 180, 361)
lat = np.linspace(-90, 90, 181)

lon2d, lat2d = np.meshgrid(lon, lat)

B = (
    45000
    + 15000 * np.sin(np.radians(lat2d))
    + 8000 * np.cos(np.radians(lon2d / 2))
)

# Figure
fig = plt.figure(figsize=(12,6))

ax = plt.axes(projection=ccrs.Robinson())

# Filled contours
cf = ax.contourf(
    lon2d,
    lat2d,
    B,
    20,
    transform=ccrs.PlateCarree(),
    cmap='viridis'
)

# Contour lines
cs = ax.contour(
    lon2d,
    lat2d,
    B,
    levels=np.arange(25000,70000,5000),
    colors='white',
    linewidths=1,
    transform=ccrs.PlateCarree()
)

plt.clabel(cs, inline=True, fontsize=8)

# Coastlines
ax.coastlines(color='white')

# Colorbar
cbar = plt.colorbar(cf, orientation='horizontal', pad=0.05)
cbar.set_label("F nanoTesla")

plt.title("Overview of Earth's Magnetic Field")

plt.show()