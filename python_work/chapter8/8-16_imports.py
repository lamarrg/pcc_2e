# Using a program you wrote that has one function in it, store that function in a separate file. Import the function into your main program file, and call the function using each of these approaches:

# import module_name
# from module_name import function_name
# from module_name import function_name as fn import module_name as mn
# from module_name import *

"""
for some reason, import statements are not working as they should
"""

unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# print('example 1')
# import printing_functions
# printing_functions.print_models(unprinted_designs, completed_models)

print('example 2')
# from printing_functions import print_models
# print_models(unprinted_designs, completed_models)

print('example 4')
import printing_functions as grr
grr.print_models(unprinted_designs, completed_models)


