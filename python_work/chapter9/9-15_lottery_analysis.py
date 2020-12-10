# You can use a loop to see how hard it might be to win the kind of lottery you just modeled. Make a list or tuple called my_ticket. Write a loop that keeps pulling numbers until your ticket wins. Print a message reporting how many times the loop had to run to give you a winning ticket.

import random

num_pool = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e']


def draw_nums(num_list):
    drawn_nums = []
    for i in range(1, 5):
        selected_num = random.choice(num_list)
        # removing selected number from list so it does not get picked a second time
        num_list.remove(selected_num)
        drawn_nums.append(selected_num)
    # returning a set as it is much easier to compare sets than lists as no specific order is needed
    return set(drawn_nums)


print('##########')
my_ticket = draw_nums(num_pool[:])
print(f'My winning numbers are {my_ticket}')

count = 0
while True:
    lotto_drawing = draw_nums(num_pool[:])
    # print(f'my ticket {my_ticket}')
    print(f'lotto drawing - {lotto_drawing}')
    if my_ticket == lotto_drawing:
        # if my_ticket equals lotto=drawing, you have won!
        print(f'You have won! Your numbers are {my_ticket}')
        print(f'It took {count} drawings for this to happen!')
        break
    else:
        print('You did not win, try again\n')
        # increase loop count
        count += 1


