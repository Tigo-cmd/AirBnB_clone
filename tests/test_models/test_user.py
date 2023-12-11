#!/usr/bin/python3
"""This module defines unit tests for the 'User' class."""

import unittest
from models.user import User


class Test_User(unittest.TestCase):
    """
    Set up a list to store instances before running the tests.
    """
    instance = ""

    @classmethod
    def setUpClass(cls) -> None:
        """
        Set up a list to store instances before running the tests.
        """
        cls.instances = []

    @classmethod
    def tearDownClass(cls) -> None:
        """
        Clear the list of instances after all tests have been executed.
        """
        cls.instances.clear()

    def setUp(self) -> None:
        """
        Initialize a 'User' instance with specific attributes before each test.
        """
        self.instance = User(
            email="text@mail.com",
            password="qwerty254",
            first_name="bon",
            last_name="emma",
        )

    def tearDown(self) -> None:
        """
        Clean up by deleting the current 'User' instance and clearing the list
        of instances after each test.
        """
        del self.instance
        self.instances.clear()

    def test_instance_creation(self):
        """
        Test if an instance of the 'User' class can be created successfully.
        """
        self.assertIsInstance(self.instance, User)

    def test_user_attributes(self):
        """
        test if attributes of the 'User' class are correctly set.
        """
        self.assertEqual(self.instance.email, "text@mail.com")
        self.assertEqual(self.instance.password, "qwerty254")
        self.assertEqual(self.instance.first_name, "bon")
        self.assertEqual(self.instance.last_name, "emma")
