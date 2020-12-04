# You don’t have to limit the number of tests you create to ten. If you want to try more comparisons, write more tests and add them to conditional_tests.py. Have at least one True and one False result for each of the following:
# • Tests for equality and inequality with strings
print('arrrrgh' == 'arrrrrgh')

# • Tests using the lower() method
name = 'Tracy'
print(name == name.lower())

# • Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to
print(12 == 12)
print(34 != 4)
print(45 > 8)
print(65 < 109)
print(54 >= 54)
print(73 <= 76)

# • Tests using the and keyword and the or keyword
print(65 < 109 and 31 >= 54)
print(65 < 109 or 31 >= 54)

# • Test whether an item is in a list
valuables = ['gold', 'silver', 'iron', 'diamond']
print('gold' in valuables)

# • Test whether an item is not in a list
tv_shows = ['oak island', 'mandalorian', 'blacklist']
print('firefly' not in tv_shows)
