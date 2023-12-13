import matplotlib.pyplot as plt
import numpy as np

# Dummy data
time_of_operation = np.linspace(0, 10, 100)  # 0 to 10 seconds
deviation = np.sqrt(time_of_operation)  # Deviation increases with operation time
measurement_intensity = np.linspace(1, 10, 100)  # Some arbitrary scale for intensity

# Create figure and primary y-axis
fig, ax1 = plt.subplots()

# Plot deviation vs time
color = 'tab:red'
ax1.set_xlabel('Duration of Operation Before Measurement (seconds)')
ax1.set_ylabel('Degree of Deviation from Quantum Mechanics', color=color)
ax1.plot(time_of_operation, deviation, color=color)
ax1.tick_params(axis='y', labelcolor=color)

# Create secondary y-axis for measurement intensity
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Measurement Intensity', color=color)
ax2.plot(time_of_operation, measurement_intensity, color=color, linestyle='--')
ax2.tick_params(axis='y', labelcolor=color)

# Title
plt.title('Deviation from Quantum Mechanical Paradigm Over Time with Varying Measurement Intensity')

# Legend (we are using the labels as legend)
ax1.legend(['Deviation'], loc='upper left')
ax2.legend(['Measurement Intensity'], loc='upper right')

# Save figure in local directory as "img.png"
plt.savefig("img.png")
plt.close()