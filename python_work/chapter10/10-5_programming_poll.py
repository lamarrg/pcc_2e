# Write a while loop that asks people why they like programming. Each time someone enters a reason, add their reason to a file that stores all the responses.

filename = 'like_programming.txt'

print('Enter "q" at any point to quit.')

while True:

    reason = input('Why do you like programming? ')

    if reason == 'q':
        break

    with open(filename, 'a') as text_file:
        text_file.write(f'{reason}\n')



