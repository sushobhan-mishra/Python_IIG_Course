import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Generate synthetic distance data (km)
# -------------------------------
x = np.linspace(-100, 100, 500)

# -------------------------------
# Define geophysical parameters
# -------------------------------
depth = 20        # depth to source (km)
amplitude = 100   # anomaly amplitude (nT)

# -------------------------------
# Magnetic anomaly model (simple dipole-like response)
# -------------------------------
anomaly = amplitude * (depth**2) / (x**2 + depth**2)

# Add small random noise to simulate real data
noise = np.random.normal(0, 2, size=x.shape)
observed_anomaly = anomaly + noise

# -------------------------------
# Plot the results
# -------------------------------
plt.figure(figsize=(10, 5))
plt.plot(x, observed_anomaly, label="Observed Magnetic Anomaly", linewidth=1)
plt.plot(x, anomaly, label="True Model", linestyle='--', linewidth=2)

plt.xlabel("Distance (km)")
plt.ylabel("Magnetic Anomaly (nT)")
plt.title("Synthetic Magnetic Anomaly Profile")
plt.legend()
plt.grid()

plt.show()