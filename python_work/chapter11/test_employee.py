import unittest
from employee import Employee


class TestEmployee(unittest.TestCase):
    def setUp(self):
        """
        Create an employee instance
        """
        self.danny = Employee('Danny', 'Alex', 7000)

    def test_give_default_raise(self):
        """
        Test default raise
        """
        self.danny.give_raise()
        self.assertEqual(self.danny.salary, 12000)

    def test_give_custom_raise(self):
        """
        Test custom raise
        """
        self.danny.give_raise(3000)
        self.assertEqual(self.danny.salary, 10000)


if __name__ == '__main__':
    unittest.main()


