import matplotlib.pyplot as plt

# Data for plotting
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
butterfly_population = [14, 15, 18, 20, 25, 30, 26, 22, 40, 60, 45, 16]
peak_migration_start = 'Aug'
peak_migration_end = 'Oct'

# Create figure and axis
fig, ax = plt.subplots()

# Plot the line graph for estimated monarch butterfly population size
ax.plot(months, butterfly_population, label='Estimated Monarch Butterfly Population Size', marker='o')

# Highlight the peak migration period
peak_start_index = months.index(peak_migration_start)
peak_end_index = months.index(peak_migration_end)
ax.axvspan(peak_start_index, peak_end_index + 1, color='lightgrey', alpha=0.5, label='Peak Migration Period')

# Annotate the peak migration
ax.annotate('Peak Migration to Mexico', xy=('Oct', 60), xytext=('Nov', 65),
             arrowprops=dict(facecolor='black', shrink=0.05))

# Y-axis label
ax.set_ylabel('Number of Monarch Butterflies (in millions)')

# X-axis label
ax.set_xlabel('Time of Year')

# Adding title
ax.set_title('Annual Monarch Butterfly Migration Journey')

# Set Y-axis scale
ax.set_ylim(0, max(butterfly_population) + 5)

# Add more information on Y-axis to indicate number is in millions
ax.set_yticklabels(['{:.0f}M'.format(x) for x in ax.get_yticks()])

# Adding legend
ax.legend()

# Saving the plot as an image file
plt.savefig('img.png', format='png')

plt.close()  # Close the figure to prevent it from displaying