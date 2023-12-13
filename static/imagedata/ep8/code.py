import matplotlib.pyplot as plt

# Data for the graph
years = [0, 1, 3, 5, 7, 10, 15, 20]
frequency = [0, 2, 10, 25, 45, 70, 90, 98]

# Create the figure and the axis
fig, ax = plt.subplots()

# Plot the data
ax.plot(years, frequency, '-o', label='Pesticide Resistance')

# Label the axes
ax.set_xlabel('Time (Years)')
ax.set_ylabel('Frequency of Resistance Alleles in Insect Population (%)')

# Set the range for the axes
ax.set_xlim(0, 20)
ax.set_ylim(0, 100)

# Set the title of the graph
ax.set_title('Frequency of Pesticide Resistance Alleles Over Time')

# Add grid for better readability
ax.grid(True)

# Save the figure
plt.savefig('img.png')