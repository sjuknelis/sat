import matplotlib.pyplot as plt
import numpy as np

# Data Simulation
months = np.arange(1, 13)
# Assuming a sinusoidal migration pattern for illustrative purposes
migration_distance = 3000 * np.abs(np.sin((months - 5) * 2 * np.pi / 12))
generation_changes = np.array([5, 7, 9, 11])  # hypothetical generational change months
generations = np.zeros_like(months)
current_generation = 1
for m in range(len(months)):
    generations[m] = current_generation
    if months[m] in generation_changes:
        current_generation += 1

# Start Plotting
fig, ax1 = plt.subplots()

# Plot migration distance - Line Graph
color = 'tab:orange'
ax1.set_xlabel('Time of Year (months)')
ax1.set_ylabel('Distance Traveled (in miles)', color=color)
ln1 = ax1.plot(months, migration_distance, color=color, label='Migration Distance')
ax1.tick_params(axis='y', labelcolor=color)
ax1.set_xticks(months)
ax1.set_xticklabels(['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
ax1.set_ylim(0, 3200)
ax1.set_yticks(np.arange(0, 3201, 500))

# Plot Generation Number - Bar Graph
ax2 = ax1.twinx()
color = 'tab:blue'
ax2.set_ylabel('Generation Number', color=color)
ln2 = ax2.bar(months, generations, color=['black', 'lightgray', 'gray', 'darkgrey'], alpha=0.6, label='Generation Number')
ax2.tick_params(axis='y', labelcolor=color)
ax2.set_yticks([1, 2, 3, 4])

# Annotations
ax1.annotate('Start of Journey - Northern United States/Canada',
             xy=(5, 0), xytext=(3, 1000),
             arrowprops=dict(facecolor='black', shrink=0.05))
ax1.annotate('Arrival in Central Mexico', xy=(11, migration_distance[10]), xytext=(9, migration_distance[10] + 500),
             arrowprops=dict(facecolor='black', shrink=0.05))
ax1.annotate('Return to Start Point', xy=(3, 0), xytext=(1, 1000),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Legend and title
fig.suptitle('Monarch Butterfly Migration Distance and Generational Relay')
fig.legend(loc="lower center", bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True, ncol=5)

# Save the plot as image
plt.savefig('img.png', bbox_inches='tight')
plt.close()