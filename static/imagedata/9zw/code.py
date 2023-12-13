import matplotlib.pyplot as plt

# Define the data for the X-axis and Y-axis
x = ["50,000 Years Ago", "10,000 Years Ago", "5,000 Years Ago", "1,000 Years Ago", "500 Years Ago", "Industrial Revolution", "Digital Age", "Present Day"]
y_bio = [0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2, 0.2]  # Flat line for Biological Evolution
y_tech = [0.2, 0.2, 0.4, 0.6, 0.8, 1.2, 1.8, 2.4]  # Values are arbitrary just to show the trend

# Mapping x labels to an integer index for plotting
x_values = range(len(x))

# Create the plot
plt.figure(figsize=(10, 5))

# Add lines to the plot
plt.plot(x_values, y_bio, label="Biological Evolution", marker='o')
plt.plot(x_values, y_tech, label="Technological Influence", marker='o')

# Mark significant points with annotations
plt.annotate('Written Language', xy=(2, y_tech[2]), xytext=(2-0.5, y_tech[2]+0.4),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('Print Revolution', xy=(4, y_tech[4]), xytext=(4-0.5, y_tech[4]+0.4),
             arrowprops=dict(facecolor='black', arrowstyle='->'))
plt.annotate('Digital Age', xy=(6, y_tech[6]), xytext=(6-0.5, y_tech[6]+0.4),
             arrowprops=dict(facecolor='black', arrowstyle='->'))

# Title and labels
plt.title("Evolution of the Human Brain Over Time in Relation to Technological Advancements")
plt.xticks(x_values, x)  # Set the X-axis to show our labels
plt.xlabel("Time (Years Ago)")
plt.ylabel("Human Brain Development Indicators")

# Add legends
plt.legend()

# Flip the x-axis to show the oldest times on the right
plt.gca().invert_xaxis()

# Save the figure to the local directory
plt.savefig("img.png")