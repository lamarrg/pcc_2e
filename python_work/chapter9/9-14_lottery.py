# Make a list or tuple containing a series of 10 numbers and five letters. Randomly select four numbers or letters from the list and print a message saying that any ticket matching these four numbers or letters wins a prize.

import random

num_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']

selected_nums = []


def num_selection(num_list):
    for i in range(1, 5):
        trina = random.choice(num_list)
        # removing num from list so it does not get picked a second time
        num_list.remove(trina)
        selected_nums.append(trina)
    print(num_list)
    print(selected_nums)


# by the way lottery works, using a list copy because each selection has to be unique.
# cannot have the a duplicate in core numbers
num_selection(num_pool[:])

