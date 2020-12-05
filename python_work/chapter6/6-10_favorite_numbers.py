# Modify your program from Exercise 6-2 (page 99) so each person can have more than one favorite number. Then print each per- son’s name along with their favorite numbers.

favorite_numbers = {
    'trevor': [98, 12, 934, 4829],
    'kinsey': [8893, 43, 604],
    'macie': [7, 563, 284],
    'frank': [834, 495, 727832],
    'tennyson': [9, 32]
}

for num in favorite_numbers:
    print(f'{num}\'s favorite places:')
    for fav in favorite_numbers[num]:
        print(f'\t{fav}')


