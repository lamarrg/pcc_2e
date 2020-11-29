# You just found a bigger dinner table, so now more space is available. Think of three more guests to invite to dinner.
# • Start with your program from Exercise 3-4 or Exercise 3-5. Add a print() call to the end of your program informing people that you found a bigger dinner table.
# • Use insert() to add one new guest to the beginning of your list.
# • Use insert() to add one new guest to the middle of your list.
# • Use append() to add one new guest to the end of your list.
# • Print a new set of invitation messages, one for each person in your list.

dinner_invitees = ["Irdris Elba", "Neil DeGrasse Tyson", "Angela Timbur", "Salma Hayek"]

print(f'{dinner_invitees[0]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[1]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[2]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[3]}, would you like to come to dinner?!?!')

print(f'{dinner_invitees[0]} can\'t make it....')

dinner_invitees[0] = 'Dwayne Johnson'

print(f'{dinner_invitees[0]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[1]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[2]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[3]}, would you like to come to dinner?!?!')

print(f'And now we have a bigger table!!!')

dinner_invitees.append("Malala")
dinner_invitees.append("Cher")
dinner_invitees.append("Barack Obama")

print(f'{dinner_invitees[0]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[1]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[2]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[3]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[4]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[5]}, would you like to come to dinner?!?!')
print(f'{dinner_invitees[6]}, would you like to come to dinner?!?!')

