# An administrator is a special kind of user. Write a class called Admin that inherits from the User class you wrote in Exercise 9-3 (page 162)
# or Exercise 9-5 (page 167). Add an attribute, privileges, that stores a list
# of strings like "can add post", "can delete post", "can ban user", and so on. Write a method called show_privileges() that lists the administrator’s set of privileges. Create an instance of Admin, and call your method.


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
        self.privileges = ["can add post", "can delete post", "can ban user"]


terry = Admin('terry', 'grant', 'TG', 'WY')
print(terry.privileges)
