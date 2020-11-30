# Using one of the programs you wrote in this chapter, add several lines to the end of the program that do the following:
# • Print the message The first three items in the list are:. Then use a slice to print the first three items from that program’s list.
threes = [num*3 for num in range(1, 31)]
print(f"The first three items in the list are:{threes[:3]}")

# • Print the message Three items from the middle of the list are:. Use a slice to print three items from the middle of the list.
print(f"The middle three items in the list are:{threes[5:8]}")

# • Print the message The last three items in the list are:. Use a slice to print the last three items in the list.
print(f"The last three items in the list are:{threes[-3:]}")

