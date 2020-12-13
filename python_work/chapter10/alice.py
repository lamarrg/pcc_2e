filename = 'alice.txt'

# with open(filename, encoding='utf-8') as f:
#     contents = f.read()

# -------------------------

# try:
#     with open(filename, encoding='utf-8') as f:
#         contents = f.read()
# except FileNotFoundError:
#     print(f'Sorry, the file {filename} does not exist')

# -------------------------

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f'Sorry, the file {filename} does not exist')
else:
    # count the approx number of words int eh file
    words = contents.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")


