# Think of at least three kinds of your favorite pizza. Store these pizza names in a list, and then use a for loop to print the name of each pizza.
pizzas = ['combo', 'pepperoni', 'sausage', 'cheese']

for pizza in pizzas:
    print(pizza)

# • Modify your for loop to print a sentence using the name of the pizza instead of printing just the name of the pizza. For each pizza you should have one line of output containing a simple statement like I like pepperoni pizza.
for pizza in pizzas:
    print(f"Mmmm... can\'t wait to have a {pizza} pizza!")

# • Add a line at the end of your program, outside the for loop, that states how much you like pizza. The output should consist of three or more lines about the kinds of pizza you like and then an additional sentence, such as I really love pizza!
for pizza in pizzas:
    print(f"I really like {pizza} pizza!")
print("Can you tell that I really like pizza?")
