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