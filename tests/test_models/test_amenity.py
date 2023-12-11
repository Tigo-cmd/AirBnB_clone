#!/usr/bin/python3
"""unittest test cases 'models.amenity' module.."""

import unittest
from models.amenity import Amenity


class Test_Amenity(unittest.TestCase):
    """
    unittest test cases for the 'Amenity' class from the 'models.amenity'
    module.
    """
    def test_instance_creation(self):
        """
        Checks if an instance of the 'Amenity' class can be created
        successfully.
        """
        instance = Amenity()
        self.assertIsInstance(instance, Amenity)

    def test_amenity_attributes(self):
        """
        Verifies that the 'name' attribute of the 'Amenity' class is correctly
        set when creating an instance with a name parameter.
        """
        instance = Amenity(name="pool")
        self.assertEqual(instance.name, "pool")
