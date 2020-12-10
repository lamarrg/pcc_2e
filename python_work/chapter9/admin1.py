from user1 import User
from privileges1 import Privileges


class Admin(User):
    def __init__(self, first_name, last_name, username, state):
        super().__init__(first_name, last_name, username, state)
        self.privileges = Privileges()

