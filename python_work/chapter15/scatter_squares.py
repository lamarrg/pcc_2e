import matplotlib.pyplot as plt

# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(2, 4, s=200)
#
# # set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # set size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()

# ----------------------------------

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
#
# plt.style.use('seaborn')
# fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, s=200)
#
# # set chart title and label axes
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Value", fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)
#
# # set size of tick labels
# ax.tick_params(axis='both', which='major', labelsize=14)
#
# plt.show()


# -------------------------------------

# calculating data automatically
import matplotlib.pyplot as plt

x_values = range(1, 1001)
y_values = [x**2 for x in x_values]

plt.style.use('seaborn')
fig, ax = plt.subplots()
# ax.scatter(x_values, y_values, c='red', s=10)
# ax.scatter(x_values, y_values, c=(0, 0.8, 0), s=10)

# using colormaps
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)

# set chart title and label axes
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("Square of Value", fontsize=14)

# set size of tick labels
ax.tick_params(axis='both', which='major', labelsize=14)

# set range for each axis
ax.axis([0, 1100, 0, 1100000])

# plt.show()
plt.savefig('saveMyPlot.png', bbox_inches='tight')

