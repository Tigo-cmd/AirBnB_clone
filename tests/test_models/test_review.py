#!/usr/bin/python3
"""This module defines unit tests for the Review class."""

import unittest
from models.review import Review


class Test_Review(unittest.TestCase):
    """
    This module defines unit tests for the 'Review' class.
    """
    def test_instance_creation(self):
        """
        Checks if an instance of the 'Review' class can be created
        successfully.
        """
        instance = Review()
        self.assertIsInstance(instance, Review)

    def test_review_attributes(self):
        """
        Verifies that the 'place_id,' 'user_id,' and 'text' attributes of the
        'Review' class are correctly set when creating an instance with these
        parameters.
        """
        instance = Review(place_id="Penthouse123",
                          user_id="gabby_com",
                          text="Great place to stay!"
                          )
        self.assertEqual(instance.place_id, "Penthouse123")
        self.assertEqual(instance.user_id, "gabby_com")
        self.assertEqual(instance.text, "Great place to stay!")
