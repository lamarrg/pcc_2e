import json

filename = 'favorite_number.json'

try:
    with open(filename) as f:
        fav_num = json.load(f)
except FileNotFoundError:
    print('That file does not exist...')
else:
    print(f"I know your favorite number! It’s {fav_num}.")


