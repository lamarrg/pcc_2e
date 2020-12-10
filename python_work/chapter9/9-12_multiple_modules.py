# Store the User class in one module, and store the Privileges and Admin classes in a separate module. In a separate file, create an Admin instance and call show_privileges() to show that everything is still working correctly.

from admin1 import Admin

terry = Admin('gloria', 'endname', 'ghostme', 'OR')
terry.privileges.show_privileges()


