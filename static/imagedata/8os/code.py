import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# This code is a dummy representation and may not correspond to real-world data.
# Full-fledged code would require precise latitudes, longitudes, and months of each event.

# Base map setup with arbitrary coordinates for illustration purposes
fig, ax = plt.subplots(figsize=(10, 5))
ax.set_xlim(-130, -60)
ax.set_ylim(10, 60)
ax.axis('off')

# Draw the migration path with fake coordinates
migration_path = mpatches.FancyArrowPatch((70, 70), (25, 25),
                                          color="orange", mutation_scale=10,
                                          lw=2, arrowstyle="->")
ax.add_patch(migration_path)

# Add oyamel fir forests
ax.text(25, 25, 'Oyamel Fir Forests', ha='center', va='center', fontsize=8)
ax.scatter(25, 25, color='green')

# Add breeding and feeding grounds
ax.scatter([60, 65], [45, 50], color='blue', label='Breeding/Feeding grounds')

# Timeline for migratory cycle
timeline_ax = fig.add_axes([0.1, 0.1, 0.8, 0.1], frameon=False)
timeline_ax.set_xlim(0, 12)
timeline_ax.set_ylim(0, 1)
timeline_ax.axis('off')

# Month labels and ticks for the timeline
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
timeline_ax.set_xticks(range(1, 13))
timeline_ax.set_xticklabels(months)

# Generational labels
generations = ['1st Gen: Mar - Apr', '2nd Gen: May - Jun', '3rd Gen: Jul - Aug', '4th Gen: Sep - Nov']

# Plotting generations on timeline
for i, gen in enumerate(generations):
    timeline_ax.text((i + 1) * 3 - 1.5, 0.5, gen, ha='center', va='center', fontsize=8)

# Conservation highlights
conservation_areas = [60, 55] # Dummy coordinates for conservation areas
for area in conservation_areas:
    ax.scatter(area, 50, color='red', label='Conservation areas')

# Adding legends
handles, labels = ax.get_legend_handles_labels()
fig.legend(handles, labels, loc='upper left')

# Save the image
plt.savefig('img.png')