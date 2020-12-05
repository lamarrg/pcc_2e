# A Python dictionary can be used to model an actual dictionary. However, to avoid confusion, let’s call it a glossary.
# • Think of five programming words you’ve learned about in the previous chapters. Use these words as the keys in your glossary, and store their meanings as values.
# • Print each word and its meaning as neatly formatted output. You might print the word followed by a colon and then its meaning, or print the word on one line and then print its meaning indented on a second line. Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

glossary = {
    'variable': 'Variables are often described as boxes you can store values in',
    'string': 'A string is a series of characters',
    'float': 'Python calls any number with a decimal point a float.',
    'constant': 'A constant is like a variable whose value stays the same throughout the life of a program.',
    'list': 'A list is a collection of items in a particular order'
}

print(f"variable: {glossary['variable']}\n")
print(f"string: {glossary['string']}\n")
print(f"float: {glossary['float']}\n")
print(f"constant: {glossary['constant']}\n")
print(f"list: {glossary['list']}")
