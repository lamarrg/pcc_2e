# Write a separate Privileges class. The class should have one attribute, privileges, that stores a list of strings as described in Exercise 9-7. Move the show_privileges() method to this class. Make a Privileges instance as an attribute in the Admin class. Create a new instance of Admin and use your method to show its privileges.

class Privileges:
    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    def show_privileges(self):
        print(self.privileges)


class User:
    def __init__(self, first_name, last_name, username, state):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.state = state
        self.login_attempts = 0

    def describe_user(self):
        print(f'{self.first_name} {self.last_name}, your username is {self.username}.')

    def greet_user(self):
        print(f'{self.first_name}, welcome to the platform!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


class Admin(User):
    def __init__(self, first_name, last_name, username, state):
        super().__init__(first_name, last_name, username, state)
        self.privileges = Privileges()


terry = Admin('terry', 'grant', 'TG', 'WY')
terry.privileges.show_privileges()

