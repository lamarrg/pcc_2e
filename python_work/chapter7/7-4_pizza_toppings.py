# Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping, print a message saying you’ll add that topping to their pizza.

prompt = 'Please enter a topping you would like on your pizza.'
prompt += '\nEnter \'quit\' when you are done. '

topping = ''
while topping != 'quit':
    topping = input(prompt)

    if topping != 'quit':
        print(f'{topping} will be added to your pizza.')
