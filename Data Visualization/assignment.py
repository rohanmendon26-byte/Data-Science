import matplotlib.pyplot as plt

# 10 years of hypothetical runs
years = [2015, 2016, 2017, 2018, 2019,
         2020, 2021, 2022, 2023, 2024]

kohli = [1200, 1350, 1450, 1600, 1750, 1400, 1550, 1700, 1850, 1950]
rohit = [1100, 1250, 1300, 1500, 1650, 1350, 1450, 1600, 1750, 1900]
sehwag = [1000, 1150, 1250, 1350, 1450, 1200, 1100, 1050, 950, 900]

# Custom style
plt.style.use('ggplot')

# Create plot
plt.figure(figsize=(10, 6))

plt.plot(years, kohli,
         color='blue',
         linestyle='-',
         marker='o',
         linewidth=2,
         label='Virat Kohli')

plt.plot(years, rohit,
         color='red',
         linestyle='--',
         marker='s',
         linewidth=2,
         label='Rohit Sharma')

plt.plot(years, sehwag,
         color='green',
         linestyle=':',
         marker='^',
         linewidth=2,
         label='Virender Sehwag')

# Labels and title
plt.xlabel('Year')
plt.ylabel('Runs')
plt.title('Hypothetical Runs Comparison Over 10 Years')

# Legend
plt.legend()

# Grid
plt.grid(True)

# Display plot
plt.show()