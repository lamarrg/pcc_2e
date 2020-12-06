# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

sandwich_orders = ['reuben', 'pastrami', 'pastrami', 'turkey', 'egg salad', 'pastrami', 'grilled cheese']

finished_sandwiches = []

print('The deli has run out of pastrami')

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich_orders.remove(sandwich)
        print(f'I made your {sandwich} sandwich')
        finished_sandwiches.append(sandwich)

print('Sandwiches that have been made:')
for sandwich in finished_sandwiches:
    print(f'{sandwich}')


