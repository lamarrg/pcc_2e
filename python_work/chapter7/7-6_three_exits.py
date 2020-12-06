# Write different versions of either Exercise 7-4 or Exercise 7-5 that do each of the following at least once:
# • Use a conditional test in the while statement to stop the loop.
# • Use an active variable to control how long the loop runs.
# • Use a break statement to exit the loop when the user enters a 'quit' value

prompt = 'Please enter your age, and we will tell you the ticket price.'
prompt += '\nEnter \'quit\' when you are done. '

# age = ''
# while age != 'quit':
#     age = input(prompt)
#
#     if age == 'quit':
#         break
#
#     age = int(age)
#     if age <= 3:
#         print('The cost of your ticket is $0.')
#     elif age > 3 and age <= 12:
#         print('The cost of your ticket is $10.')
#     else:
#         print('The cost of your ticket is $15.')

active = True
age = ''
while active:
    age = input(prompt)

    if age == 'quit':
        active = False
    else:
        age = int(age)
        if age <= 3:
            print('The cost of your ticket is $0.')
        elif age > 3 and age <= 12:
            print('The cost of your ticket is $10.')
        else:
            print('The cost of your ticket is $15.')

