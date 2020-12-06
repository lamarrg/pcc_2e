# A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their age, and then tell them the cost of their movie ticket.

prompt = 'Please enter your age, and we will tell you the ticket price.'
prompt += '\nEnter \'quit\' when you are done. '

age = ''
while age != 'quit':
    age = input(prompt)

    if age != 'quit':
        age = int(age)
        if age <= 3:
            print('The cost of your ticket is $0.')
        elif age > 3 and age <= 12:
            print('The cost of your ticket is $10.')
        else:
            print('The cost of your ticket is $15.')

