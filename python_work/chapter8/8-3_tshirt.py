# Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. The function should print a sentence summarizing the size of the shirt and the message printed on it.
# Call the function once using positional arguments to make a shirt. Call the function a second time using keyword arguments.

def make_shirt(size, message):
    print(f'Request for tshirt of size {size}, with message "{message}" has been logged.')


make_shirt('XL', 'See me, love me!')
make_shirt(message='Do as I say, not as I get caught for.', size='S')
