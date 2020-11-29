# You just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two names remain in your list. Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
# • Print a message to each of the two people still on your list, letting them know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.

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

print("I have been deceived... I can only invite 2 people.")

print(f"I'm sorry {dinner_invitees.pop(0)}, I can no longer invite you to dinner. My apologies.")
print(f"I'm sorry {dinner_invitees.pop()}, I can no longer invite you to dinner. My apologies.")
print(f"I'm sorry {dinner_invitees.pop()}, I can no longer invite you to dinner. My apologies.")
print(f"I'm sorry {dinner_invitees.pop()}, I can no longer invite you to dinner. My apologies.")
print(f"I'm sorry {dinner_invitees.pop()}, I can no longer invite you to dinner. My apologies.")

print(f"{dinner_invitees[0]}, you made the cut!")
print(f"{dinner_invitees[1]}, you made the cut!")

# delete remaining guests
del dinner_invitees[0]
del dinner_invitees[0]

# confirm the list is empty
print(dinner_invitees)
