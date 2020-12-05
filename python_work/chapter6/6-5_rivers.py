# Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
# • Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# • Use a loop to print the name of each river included in the dictionary.
# • Use a loop to print the name of each country included in the dictionary.

waterways = {
    'USA': 'Missouri',
    'China': 'Yangtze River',
    'South America': 'Amazon',
    'Congo': 'Zaire'
}

for k, v in waterways.items():
    print(f'The {v} runs through {k}')

for item in waterways.values():
    print(item)

for item in waterways:
    print(item)

