import matplotlib.pyplot as plt

years = [1980, 1985, 1990, 1995, 2000, 2005, 2010, 2015, 2020]
population = [20, 18, 16, 14, 12, 10, 8, 6, 4]
conservation_efforts = [0, 1, 2, 3, 4, 5, 6, 7, 8]

plt.plot(years, population, label='Population Size')
plt.plot(years, conservation_efforts, label='Conservation Efforts')

plt.xlabel('Years')
plt.ylabel('Population Size (millions of butterflies)')
plt.title('Population of Monarch Butterflies Over Time')
plt.legend()

plt.savefig('img.png')