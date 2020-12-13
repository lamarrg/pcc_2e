import json

filename = 'favorite_number.json'
fav_num = input('What is your favorite number? ')

with open(filename, 'w') as f:
    json.dump(fav_num, f)



