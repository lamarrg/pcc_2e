# Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input('Please enter a number: ')

if int(number) % 10 == 0:
    print('Your number is a multiple of 10.')
else:
    print('Your number is NOT a multiple of 10...')

