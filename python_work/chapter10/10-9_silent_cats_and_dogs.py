# Modify your except block in Exercise 10-8 to fail silently if either file is missing.

def read_names(filename):
    try:
        with open(filename) as f:
            content = f.read()
            print(content)
    except FileNotFoundError:
        pass

read_names('cats.txt')

read_names('cats2.txt')

read_names('dogs.txt')


