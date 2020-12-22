# A number raised to the third power is a cube. Plot the first five cubic numbers, and then plot the first 5000 cubic numbers.

import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
x_values = range(1, 5001)

y_values = [x**3 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s=20)

ax.set_title("Cube Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Cube of Value", fontsize=14)

ax.tick_params(axis='both', which='major', labelsize=14)

plt.show()

