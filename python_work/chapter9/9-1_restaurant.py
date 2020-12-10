# Make a class called Restaurant. The __init__() method for Restaurant should store two attributes: a restaurant_name and a cuisine_type. Make a method called describe_restaurant() that prints these two pieces of information, and a method called open_restaurant() that prints a message indi- cating that the restaurant is open.
# Make an instance called restaurant from your class. Print the two attri- butes individually, and then call both methods.

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


restaurant = Restaurant('Buddy\'s Place', 'comfort food')

print(restaurant.restaurant_name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()
