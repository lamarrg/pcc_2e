# Write a program that polls users about their dream vaca- tion. Write a prompt similar to If you could visit one place in the world, where would you go? Include a block of code that prints the results of the poll.


prompt1 = 'What is your name? '
prompt2 = 'If you could go anywhere in the world, where would you go? '


polling_active = True
polled = {}

while polling_active:
    name = input(prompt1)
    destination = input(prompt2)

    polled[name] = destination

    keep_going = input('Would you like to keep going? yes/no ')
    if keep_going == 'no':
        polling_active = False

for k, v in polled.items():
    print(f'{k} would like to visit {v}')



