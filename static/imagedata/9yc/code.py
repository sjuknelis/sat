import matplotlib.pyplot as plt

# Data for the x-axis
stages_of_photosynthesis = ["Light Absorption", "Water Splitting", "Energy Carrier Formation", "Carbon Fixation", "Glucose Production"]

# Arbitrary energy levels for the light-dependent reactions
energy_levels_light_dependent = [100, 80, 120, None, None]  # None for missing values

# Arbitrary energy levels for the Calvin cycle
energy_levels_calvin_cycle = [None, None, 120, 70, 50]  # None for missing values

# Create the figure and axis
fig, ax = plt.subplots()

# Plot the light-dependent reactions
ax.plot(stages_of_photosynthesis, energy_levels_light_dependent, label="Light-Dependent Reactions", color='blue', marker='o')

# Plot the Calvin cycle
ax.plot(stages_of_photosynthesis, energy_levels_calvin_cycle, label="Calvin Cycle (Light-Independent Reactions)", color='green', marker='o')

# Add icons as annotations
ax.annotate('', xy=(0, 100), xytext=(0, 110), arrowprops=dict(facecolor='yellow', shrink=0.05))
ax.text(0, 110, 'Sunlight', fontsize=9)

ax.annotate('', xy=(1, 80), xytext=(1, 75), arrowprops=dict(facecolor='lightblue', shrink=0.05))
ax.text(1, 70, 'H2O + O2', fontsize=9)

ax.annotate('', xy=(2, 120), xytext=(2, 130), arrowprops=dict(facecolor='orange', shrink=0.05))
ax.text(2, 130, 'ATP + NADPH', fontsize=9)

ax.annotate('', xy=(3, 70), xytext=(3, 60), arrowprops=dict(facecolor='brown', shrink=0.05))
ax.text(3, 55, 'CO2 Fixation', fontsize=9)

ax.text(4, 55, 'C6H12O6', fontsize=9)
ax.annotate('', xy=(4, 50), xytext=(4, 40), arrowprops=dict(facecolor='red', shrink=0.05))

# Setting the labels for x-axis and y-axis
ax.set_xlabel("Stages of Photosynthesis")
ax.set_ylabel("Relative Energy Level (Arbitrary Units)")

# Adding the title
ax.set_title("The Stages of Photosynthesis and Their Energy Changes")

# Add the legend
ax.legend()

# Add the overall chemical reaction as an inset box
reaction_text = '6CO2 + 6H2O + light energy → C6H12O6 + 6O2'
props = dict(boxstyle='round', facecolor='wheat', alpha=0.5)
ax.text(0.25, 0.25, reaction_text, transform=ax.transAxes, fontsize=10, bbox=props)

# Footnote explaining energy levels
plt.figtext(0.5, 0.01, 'Energy levels are represented in arbitrary units and show relative changes during photosynthesis.', ha="center", fontsize=8, bbox={"facecolor":"orange", "alpha":0.5, "pad":3})

# Show the graph grid
ax.grid(True)

# Adjust the plot
plt.tight_layout()

# Save the graph to a file
plt.savefig('img.png')