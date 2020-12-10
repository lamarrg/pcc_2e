# An ice cream stand is a specific kind of restaurant. Write a class called IceCreamStand that inherits from the Restaurant class you wrote in Exercise 9-1 (page 162) or Exercise 9-4 (page 167). Either version of
# the class will work; just pick the one you like better. Add an attribute called flavors that stores a list of ice cream flavors. Write a method that displays these flavors. Create an instance of IceCreamStand, and call this method.

class Restaurant:
    """creating a new restaurant"""
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine

    def describe_restaurant(self):
        """gives the restaurant name and type of food it serves"""
        print(f'{self.restaurant_name} serves {self.cuisine}.')

    def open_restaurant(self):
        """describes that the restaurant is open"""
        print(f'{self.restaurant_name} is now open.')


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine):
        super().__init__(restaurant_name, cuisine)
        self.flavors = ['vanilla', 'cookies & cream', 'caramel']

    def show_flavors(self):
        print(self.flavors)


new_stand = IceCreamStand('Scoop Scoop', 'ice cream')

print(new_stand.show_flavors())


