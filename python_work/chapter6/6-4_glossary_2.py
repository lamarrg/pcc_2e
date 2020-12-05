# Now that you know how to loop through a dictionary, clean up the code from Exercise 6-3 (page 99) by replacing your series of print() calls with a loop that runs through the dictionary’s keys and values. When you’re sure that your loop works, add five more Python terms to your glossary. When you run your program again, these new words and meanings should automatically be included in the output.

glossary = {
    'variable': 'Variables are often described as boxes you can store values in',
    'string': 'A string is a series of characters',
    'float': 'Python calls any number with a decimal point a float.',
    'constant': 'A constant is like a variable whose value stays the same throughout the life of a program.',
    'list': 'A list is a collection of items in a particular order',
    'list comprehension': 'A list comprehension combines the for loop and the creation of new elements into one line, and automatically appends each new element.',
    'slice': 'You can also work with a specific group of items in a list, which Python calls a slice.',
    'tuple': 'Python refers to values that cannot change as immutable, and an immutable list is called a tuple.',
    'conditional test': 'At the heart of every if statement is an expression that can be evaluated as True or False and is called a conditional test.',
    'boolean expression': 'A Boolean expression is just another name for a conditional test'
}

for k, v in glossary.items():
    print(f"{k}: {v}\n")

