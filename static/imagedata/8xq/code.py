import matplotlib.pyplot as plt
import numpy as np

# Sample data - replace with real data
plant_species = ['Sunflower', 'Corn', 'Rice', 'Wheat', 'Soybean']
photosynthetic_efficiency = [30, 25, 20, 15, 10]  # percent
optimal_light_wavelength = [680, 700, 650, 670, 690]  # nm
oxygen_output = [1.5, 1.2, 1.0, 0.8, 0.5]  # liters/day

# Normalize optimal light wavelength for color
wavelength_colors = (optimal_light_wavelength - np.min(optimal_light_wavelength)) / np.ptp(optimal_light_wavelength)
colors = plt.cm.viridis(wavelength_colors)

fig, ax1 = plt.subplots()

# Bar graph for photosynthetic efficiency
bars = ax1.bar(plant_species, photosynthetic_efficiency, color=colors)

# Adding the optimal light wavelength indication
for bar, wavelength in zip(bars, optimal_light_wavelength):
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width() / 2., height,
             f'{wavelength} nm', ha='center', va='bottom')

# Setting the primary y-axis label
ax1.set_ylabel('Photosynthetic Efficiency (%)')
ax1.set_xlabel('Plant Species')
ax1.set_ylim(0, 35)  # Adjust as needed

# Creating a second y-axis for oxygen output
ax2 = ax1.twinx()
ax2.plot(plant_species, oxygen_output, 'r-o')  # line graph for oxygen output
ax2.set_ylabel('Oxygen Production (liters/day)')
ax2.set_ylim(0, 2)  # Adjust as needed

# Title and Legend
plt.title('Efficiency of Photosynthesis in Various Plant Species')
ax1.legend(['Average Photosynthetic Efficiency'])
ax2.legend(['Oxygen Output (per day)'], loc='upper left')

plt.tight_layout()

# Save the graph as "img.png" in the local directory
plt.savefig("img.png")