# -------------------------------------------------------------
# Simple Gravity Anomaly Modeling and Visualization in Python
# -------------------------------------------------------------
# This script generates a synthetic Bouguer gravity anomaly
# produced by a buried spherical body and visualizes the result.
#
# Geophysical Concept:
# A dense subsurface body creates a positive gravity anomaly,
# whereas a low-density body creates a negative anomaly.
#
# Formula Used:
#
#                G * (4/3 * pi * R^3 * Δρ) * z
# Δg(x) = ---------------------------------------------
#          (x^2 + z^2)^(3/2)
#
# where:
# G   = gravitational constant
# R   = radius of buried sphere
# Δρ  = density contrast
# z   = depth to center of sphere
# x   = horizontal distance
#
# Units:
# Distance  -> meters
# Density   -> kg/m^3
# Gravity   -> mGal
# -------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------
# Parameters of buried spherical body
# -------------------------------------------------------------

G = 6.67430e-11          # Gravitational constant (m^3 kg^-1 s^-2)

radius = 2000            # Radius of sphere (m)
depth = 5000            # Depth to center of sphere (m)
density_contrast = 500   # Density contrast (kg/m^3)

# -------------------------------------------------------------
# Observation profile
# -------------------------------------------------------------

x = np.linspace(-20000, 20000, 1000)   # Horizontal distance (m)

# -------------------------------------------------------------
# Compute mass of buried sphere
# -------------------------------------------------------------

volume = (4/3) * np.pi * radius**3
mass = volume * density_contrast

# -------------------------------------------------------------
# Gravity anomaly calculation
# -------------------------------------------------------------

gravity = (G * mass * depth) / ((x**2 + depth**2)**1.5)

# Convert from m/s^2 to mGal
# 1 mGal = 1e-5 m/s^2

gravity_mgal = gravity * 1e5

# -------------------------------------------------------------
# Plotting
# -------------------------------------------------------------

plt.figure(figsize=(10, 5))

plt.plot(x / 1000, gravity_mgal, linewidth=2)

plt.xlabel("Distance (km)", fontsize=12)
plt.ylabel("Gravity Anomaly (mGal)", fontsize=12)

plt.title("Synthetic Gravity Anomaly of a Buried Sphere", fontsize=14)

plt.grid(True)

plt.show()

# -------------------------------------------------------------
# Maximum anomaly value
# -------------------------------------------------------------

print("Maximum Gravity Anomaly: {:.3f} mGal".format(np.max(gravity_mgal)))