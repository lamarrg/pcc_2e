# Combine the two programs from Exercise 10-11 into one file. If the number is already stored, report the favorite number to the user. If not, prompt for the user’s favorite number and store it in a file. Run the program twice to see that it works.

import json
filename = 'favorite_number.json'


def favorite_num_write(filename):

    fav_num = input('What is your favorite number? ')

    with open(filename, 'w') as f:
        json.dump(fav_num, f)


def favorite_num_read(filename):
    try:
        with open(filename) as f:
            fav_num = json.load(f)
    except FileNotFoundError:
        print('It does not appear your file exists...')
        favorite_num_write(filename)
        favorite_num_read(filename)
    else:
        print(f"I know your favorite number! It’s {fav_num}.")


favorite_num_read(filename)

