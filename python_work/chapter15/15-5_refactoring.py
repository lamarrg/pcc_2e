# The fill_walk() method is lengthy. Create a new method called get_step() to determine the direction and distance for each step, and then calculate the step. You should end up with two calls to get_step() in fill_walk():
# x_step = self.get_step() y_step = self.get_step()
# This refactoring should reduce the size of fill_walk() and make the method easier to read and understand.

# refactoring is in RandomWalk2

import matplotlib.pyplot as plt

from random_walk import RandomWalk2

while True:
    # Make a random walk
    rw = RandomWalk2(5000)
    rw.fill_walk()

    # Plot the points in a walk
    plt.style.use('classic')
    fig, ax = plt.subplots(figsize=(15, 9))
    # ax.scatter(rw.x_values, rw.y_values, s=15)
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Purples, edgecolors='none', s=5)

    # Emphasize the first and last points
    ax.scatter(0, 0, c='green', edgecolors='none', s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    # Remove the axes
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()


    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break





