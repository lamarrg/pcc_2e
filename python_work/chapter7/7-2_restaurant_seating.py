# Write a program that asks the user how many people are in their dinner group. If the answer is more than eight, print a message say- ing they’ll have to wait for a table. Otherwise, report that their table is ready.

group_size = input("How many people are in your party? ")

if int(group_size) > 8:
    print('You have a large party, it will be a few momsents.')
else:
    print('Right this way...')

