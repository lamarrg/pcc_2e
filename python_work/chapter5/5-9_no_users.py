# Add an if test to hello_admin.py to make sure the list of users is not empty.
# • If the list is empty, print the message We need to find some users!
# • Remove all of the usernames from your list, and make sure the correct message is printed.

users = []  # ['honeypot', 'admin', 'tony74', 'miranda', 'serenity']

if users:
    for user in users:
        if user == 'admin':
            print('Hello admin, would you like to see the status report?')
        else:
            print(f'Hello {user}, nice to see you again.')
else:
    print('We need to find some users!')
