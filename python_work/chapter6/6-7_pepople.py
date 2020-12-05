# Start with the program you wrote for Exercise 6-1 (page 99). Make two new dictionaries representing different people, and store all three dictionaries in a list called people. Loop through your list of people. As you loop through the list, print everything you know about each person.

people = [
    {
        'first_name': 'Kelley',
        'last_name': 'BadassMOFO',
        'age': 37,
        'city': 'Denver'
    },
    {
        'first_name': 'Shelly',
        'last_name': 'Whoopsie',
        'age': 26,
        'city': 'Thornton'
    },
    {
        'first_name': 'Maverick',
        'last_name': 'Goose',
        'age': 48,
        'city': 'Golden'
    }
]

for person in people:
    for k, v in person.items():
        print(f'{k}: {v}')

