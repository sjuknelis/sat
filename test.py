import matplotlib.pyplot as plt

# creating the dataset
particles = ['Fermions', 'Bosons']
number_of_particles = [12, 5]  # There are 12 known fermions (6 quarks and 6 leptons) and 5 known bosons in the standard model

plt.bar(particles, number_of_particles, color ='blue', width = 0.4)

plt.xlabel("Types of Particles")
plt.ylabel("Number of Known Particles")
plt.title("Number of Known Fermions and Bosons in the Standard Model")
plt.show()