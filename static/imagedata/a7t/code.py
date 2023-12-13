import matplotlib.pyplot as plt

years = [2010, 2012, 2014, 2016, 2018, 2020]
population_size = [800, 1200, 1000, 900, 700, 850]

plt.plot(years, population_size, marker='o')
plt.title('Population of Monarch Butterflies in Mexico Over Time')
plt.xlabel('Year')
plt.ylabel('Population Size (thousands)')
plt.savefig('img.png')