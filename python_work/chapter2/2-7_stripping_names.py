# Use a variable to represent a person’s name, and include some whitespace characters at the beginning and end of the name. Make sure you use each character combination, "\t" and "\n", at least once.


name = " Prescient  "

print(f'{name}\n\t{name.lstrip()}\n\t{name.rstrip()}\n\t{name.strip()}')
