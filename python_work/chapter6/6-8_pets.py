# Make several dictionaries, where each dictionary represents a differ- ent pet. In each dictionary, include the kind of animal and the owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.

pets = [
    {
        'name': 'buttons',
        'owner': 'casey',
        'type': 'german shepard',
    },
    {
        'name': 'shreik',
        'owner': 'tommy',
        'type': 'owl',
    },
    {
        'name': 'dot',
        'owner': 'yeah, right',
        'type': 'animaniac',
    }
]

for pet in pets:
    for k, v in pet.items():
        print(f'{k}: {v}')
