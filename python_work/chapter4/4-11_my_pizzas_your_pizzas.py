# Start with your program from Exercise 4-1 (page 56). Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the following:
pizzas = ['combo', 'pepperoni', 'sausage', 'cheese']

friends_pizzas = pizzas[:]

# • Add a new pizza to the original list.
pizzas.append("hawaiian")

# • Add a different pizza to the list friend_pizzas.
friends_pizzas.append("veggie")

# • Prove that you have two separate lists. Print the message My favorite pizzas are:, and then use a for loop to print the first list. Print the message My friend’s favorite pizzas are:, and then use a for loop to print the sec- ond list. Make sure each new pizza is stored in the appropriate list.
print("My favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
