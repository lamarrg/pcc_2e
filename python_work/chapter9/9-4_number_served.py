# Start with your program from Exercise 9-1 (page 162). Add an attribute called number_served with a default value of 0. Create an instance called restaurant from this class. Print the number of customers the restaurant has served, and then change this value and print it again.
# Add a method called set_number_served() that lets you set the number of customers that have been served. Call this method with a new number and print the value again.
# Add a method called increment_number_served() that lets you increment the number of customers who’ve been served. Call this method with any num- ber you like that could represent how many customers were served in, say, a day of business.

class Restaurant:
    """creating a new restaurant"""
    def __init__(self, restaurant_name, cuisine):
        self.restaurant_name = restaurant_name
        self.cuisine = cuisine
        self.number_served = 0

    def describe_restaurant(self):
        """gives the restaurant name and type of food it serves"""
        print(f'{self.restaurant_name} serves {self.cuisine}.')

    def open_restaurant(self):
        """describes that the restaurant is open"""
        print(f'{self.restaurant_name} is now open.')

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number


restaurant = Restaurant('Buddy\'s Place', 'comfort food')

print(restaurant.number_served)
restaurant.number_served = 7
print(restaurant.number_served)

restaurant.set_number_served(24)

print(restaurant.number_served)

restaurant.increment_number_served(46)

print(restaurant.number_served)
