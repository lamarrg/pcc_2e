# Make a dictionary called favorite_places. Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. Loop through the dictionary, and print each person’s name and their favorite places.

favorite_places = {
    'kiki': ['maui', 'bali'],
    'dominic': ['NY', 'miami', 'vegas', 'alaska'],
    'krys': ['spokane', 'LA', 'long beach']
}

for place in favorite_places:
    print(f'{place}\'s favorite places:')
    for location in favorite_places[place]:
        print(f'\t{location}')

