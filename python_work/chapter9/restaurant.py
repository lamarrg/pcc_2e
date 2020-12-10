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