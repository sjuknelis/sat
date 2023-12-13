import matplotlib.pyplot as plt

years = [1900, 1920, 1940, 1960, 1980, 2000, 2020]
genetics_advancement = [1, 2, 3, 4, 5, 6, 7]
ocean_exploration_advancement = [1, 2, 3, 4, 5, 6, 7]
climate_change_advancement = [1, 2, 3, 4, 5, 6, 7]
space_exploration_advancement = [1, 2, 3, 4, 5, 6, 7]
ethical_considerations = [1, 2, 3, 4, 5, 6, 7]

plt.plot(years, genetics_advancement, label='Genetics and Heredity')
plt.plot(years, ocean_exploration_advancement, label='Ocean Exploration')
plt.plot(years, climate_change_advancement, label='Climate Change Study')
plt.plot(years, space_exploration_advancement, label='Space Exploration')
plt.plot(years, ethical_considerations, label='Ethical Considerations')

plt.xlabel('Years')
plt.ylabel('Level of Scientific Advancement')
plt.title('Scientific Advancements Over Time')
plt.legend()
plt.savefig('img.png')