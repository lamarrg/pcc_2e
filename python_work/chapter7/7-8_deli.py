# Make a list called sandwich_orders and fill it with the names of vari- ous sandwiches. Then make an empty list called finished_sandwiches. Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ['reuben', 'turkey', 'egg salad', 'grilled cheese']

finished_sandwiches = []

while sandwich_orders:
    for sandwich in sandwich_orders:
        sandwich_orders.remove(sandwich)
        print(f'I made your {sandwich} sandwich')
        finished_sandwiches.append(sandwich)

print('Sandwiches that have been made:')
for sandwich in finished_sandwiches:
    print(f'{sandwich}')


