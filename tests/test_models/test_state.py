#!/usr/bin/python3
# This module defines unit tests for the 'State' class

import unittest
from models.state import State


class Test_State(unittest.TestCase):
    """
    This module defines unit tests for the 'State' class.
    """
    def test_instance_creation(self):
        """
        Test if an instance of the 'State' class can be created successfully.
        """
        instance = State()
        self.assertIsInstance(instance, State)

    def test_state_attributes(self):
        """
        Test if the 'name' attribute of the 'State' class is correctly set
        when creating an instance with the 'name' parameter.
        """
        instance = State(name="Kenya")
        self.assertEqual(instance.name, "Kenya")
