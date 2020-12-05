# Make a dictionary called cities. Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. The keys for each city’s dictionary should be something like country, population, and fact. Print the name of each city and all of the infor- mation you have stored about it.

cities = {
    'Albany': {
        'country': 'USA',
        'population': 720000,
        'fact': 'I think this is the capital of NY state.'
    },
    'Rio De Janero': {
        'country': 'Brazil',
        'population': 3000000,
        'fact': 'Has the giant Jesus statue.'
    },
    'Shanghai': {
        'country': 'China',
        'population': 6700000,
        'fact': 'A very big city.'
    }
}

for city in cities:
    print(f'\n{city}:')
    for k, v in cities[city].items():
        print(f'\t{k}: {v}')




