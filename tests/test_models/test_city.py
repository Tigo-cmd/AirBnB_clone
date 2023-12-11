#!/usr/bin/python3
"""unittest test cases for the 'City' class"""

import unittest
from models.city import City


class Test_City(unittest.TestCase):
    """
    a set of unittest test cases for the 'City' class from the 'models.city'
    module.
    """
    def test_instance_creation(self):
        """
        Checks if an instance of the 'City' class can be created successfully.
        """
        instance = City()
        self.assertIsInstance(instance, City)

    def test_city_attributes(self):
        """
        Verifies that the 'state_id' and 'name' attributes of the 'City' class
        are correctly set when creating an instance with these parameters.
        """
        instance = City(state_id="NI", name="NIGERIA")
        self.assertEqual(instance.state_id, "NI")
        self.assertEqual(instance.name, "NIGERIA")
