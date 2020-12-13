# Open a blank file in your text editor and write a few lines summarizing what you’ve learned about Python so far. Start each line with the phrase In Python you can. . . . Save the file as learning_python.txt in the same directory as your exercises from this chapter. Write a program that reads the file and prints what you wrote three times. Print the contents once by reading in the entire file, once by looping over the file object, and once by storing the lines in a list and then working with them outside the with block.

filename = 'learning_python.txt'

with open(filename) as text_file:
    contents = text_file.read()
    print(contents)

print('\n----------------------\n')

with open(filename) as text_file2:
    for line in text_file2:
        print(line.strip())

print('\n----------------------\n')


filename_list = []
with open(filename) as text_file3:
    for line in text_file3:
        filename_list.append(line)

print(filename_list)
