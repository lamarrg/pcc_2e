# Write a function that accepts a list of items a person wants on a sandwich. The function should have one parameter that collects as many items as the function call provides, and it should print a summary of the sand- wich that’s being ordered. Call the function three times, using a different num- ber of arguments each time.

def make_sandwich(*args):
    print('These are going to be the ingredients on your sandwich:')
    for ingredient in args:
        print(f'\t{ingredient}')


make_sandwich('cheese', 'mustard', 'roast beef')
make_sandwich('croissant', 'cheese', 'lettuce', 'turkey')
make_sandwich('wheat bread', 'provolone', 'tomato', 'chorizo', 'relish')


