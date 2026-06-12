import pandas as pd
import matplotlib.pyplot as plt

# Read Excel file
data = pd.read_excel("Exercise 1.xlsx")

# Create figure
plt.figure(figsize=(4,10))

# Plot Sand% against Age
plt.plot(
    data["Sand%"],
    data["Age (Cal yr BP)"],
    color="black",
    linewidth=1.5
)

# Axis labels
plt.xlabel("Sand (%)")
plt.ylabel("Age (Cal yr BP)")

# Reverse age axis (older ages at bottom)
plt.gca().invert_yaxis()

# Display graph
plt.show()