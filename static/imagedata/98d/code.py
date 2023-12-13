import matplotlib.pyplot as plt
from matplotlib.offsetbox import TextArea, AnnotationBbox
import matplotlib.patches as mpatches

# Create figure and axis
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

# Part 1: Migratory Path Map
# -----------------------------------
# Note: These coordinates are illustrative and not based on actual data.
coordinates = [(-95, 50), (-90, 40), (-85, 30), (-100, 20)]
x, y = zip(*coordinates)

# Plot the migratory path on the map
ax1.plot(x, y, color='orange', linewidth=2, marker='o')
ax1.set_title("Annual Monarch Butterfly Migration Path")
ax1.set_xlim(-100, -75)  # Adjust based on actual migratory paths
ax1.set_ylim(15, 55)  # Adjust based on actual migratory paths

# Mark start and end of migration
ax1.text(x[0], y[0], 'Start of Migration', fontsize=9, verticalalignment='bottom')
ax1.text(x[-1], y[-1], 'End of Migration (Overwintering Site)', fontsize=9, verticalalignment='top')

# Add a geographical scale and grid
ax1.grid(True, linestyle='--', alpha=0.5)

# Part 2: Generational Timeline
# -----------------------------------
generations = ["1st Generation: Northern Breeding", "2nd Generation", "3rd Generation", "4th Generation: Return to Mexico"]
gen_x = range(len(generations))

# Plot the generational timeline
ax2.plot(gen_x, [1]*len(generations), color='blue', marker='s')
ax2.set_ylim(0.8, 1.3)
ax2.set_title("Generational Relay")
ax2.set_xticks(gen_x)
ax2.set_xticklabels(generations)
ax2.set_yticks([])

# Add annotations for navigation factors
time_compensation = "Time-compensated sun compass orientation"
annotation = TextArea(time_compensation)
ab = AnnotationBbox(annotation, (1.5, 1), xycoords='data', boxcoords="offset points",
                    box_alignment=(0.5, -0.1), arrowprops=dict(arrowstyle="->"))
ax2.add_artist(ab)

# Add legend to explain the generational relay
relay_patch = mpatches.Patch(color='blue', label='Generational Relay')
ax2.legend(handles=[relay_patch], loc='lower right')

# Save figure
plt.tight_layout()
plt.savefig('img.png')