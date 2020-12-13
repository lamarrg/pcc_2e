# Write a program that prompts the user for their name. When they respond, write their name to a file called guest.txt.

name = input('Welcome, what is your name? ')

filename = 'guest.txt'

with open(filename, 'w') as text_file:
    text_file.write(name)

