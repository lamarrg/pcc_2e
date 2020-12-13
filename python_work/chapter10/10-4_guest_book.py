# Write a while loop that prompts users for their name. When they enter their name, print a greeting to the screen and add a line recording their visit in a file called guest_book.txt. Make sure each entry appears on a new line in the file.

filename = 'guest_book.txt'

print('Enter "q" at any point to quit.')

while True:

    prompt = 'Add your name to the Guest Book.\n'
    prompt += 'Welcome, what is your name? '

    name = input(prompt)

    if name == 'q':
        break

    with open(filename, 'a') as text_file:
        text_file.write(f'{name}\n')

