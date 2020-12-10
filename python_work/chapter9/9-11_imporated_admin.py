# Start with your work from Exercise 9-8 (page 173). Store the classes User, Privileges, and Admin in one module. Create a sepa- rate file, make an Admin instance, and call show_privileges() to show that everything is working correctly.

from admin import Admin

terry = Admin('terry', 'grant', 'TG', 'WY')
terry.privileges.show_privileges()


