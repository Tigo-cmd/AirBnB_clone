#!/usr/bin/python3
"""This module defines unit tests for the Place class."""

import unittest
from models.place import Place


class Test_Place(unittest.TestCase):
    """
    This module defines unit tests for the 'Place' class.
    """
    def test_instance_creation(self):
        """
        Checks if an instance of the 'Place' class can be created successfully.
        """
        instance = Place()
        self.assertIsInstance(instance, Place)

    def test_place_attributes(self):
        """
        Verifies that the attributes of the 'Place' class,
        are correctly set when creating an instance with these parameters.

        """
        instance = Place(
            city_id="NI",
            user_id="qwerty",
            name="luis",
            description="allensuite",
            number_rooms=3,
            number_bathrooms=3,
            max_guest=4,
            price_by_night=200,
            latitude=27.3449,
            longitude=24.5364,
            amenity_ids=["Parking", "Wifi", "lift"],
            )
        self.assertEqual(instance.city_id, "NI")
        self.assertEqual(instance.user_id, "qwerty")
        self.assertEqual(instance.name, "luis")
        self.assertEqual(instance.description, "allensuite")
        self.assertEqual(instance.number_rooms, 3)
        self.assertEqual(instance.number_bathrooms, 3)
        self.assertEqual(instance.max_guest, 4)
        self.assertEqual(instance.price_by_night, 200)
        self.assertEqual(instance.latitude, 27.3449)
        self.assertEqual(instance.longitude, 24.5364)
        self.assertEqual(
            instance.amenity_ids,
            ["Parking", "Wifi", "lift"])
