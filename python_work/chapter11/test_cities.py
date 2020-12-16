import unittest
from city_functions import city_and_country

class CityCountryTestCase(unittest.TestCase):

    def test_city_and_country(self):
        city_country = city_and_country('Monchu Pinchu', 'Chile')
        self.assertEqual(city_country, 'Monchu Pinchu, Chile')


class CityCountryPopulationTestCase(unittest.TestCase):

    def test_city_and_country(self):
        city_country = city_and_country('Monchu Pinchu', 'Chile', '312')
        self.assertEqual(city_country, 'Monchu Pinchu, Chile - population=312')


if __name__ == '__main__':
    unittest.main()

