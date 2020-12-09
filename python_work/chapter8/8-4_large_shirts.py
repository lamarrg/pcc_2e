# Modify the make_shirt() function so that shirts are large
# by default with a message that reads I love Python. Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message.

def make_shirt(size='L', message='I love Python'):
    """Print the size of shirt and message"""
    print(f'Request for tshirt of size {size}, with message "{message}" has been logged.')


make_shirt()
make_shirt('M')
make_shirt(message='Do as I say, not as I get caught for.', size='S')
