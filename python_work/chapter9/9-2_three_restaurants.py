# Start with your class from Exercise 9-1. Create three different instances from the class, and call describe_restaurant() for each instance.

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
restaurant2 = Restaurant('Sushi A Go-Go', 'sushi')
restaurant3 = Restaurant('From The Earth', 'vegan raw')


restaurant.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()

