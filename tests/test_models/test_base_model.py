#!/usr/bin/python3
"""tests for the BaseModel class."""

import unittest
import uuid
import datetime
from models.base_model import BaseModel
from models import storage


class TestBaseModel(unittest.TestCase):
    """
    Test Class: TestBaseModel
        'setUpClass`: This class method initializes an empty list to store
        instances before running the tests.
        `tearDownClass`: After all tests are executed, this class method
        clears the list of instances.
        `setUp`: Before each individual test, this method creates three
        instances of the 'BaseModel' class.
        `tearDown`: After each test, this method removes the instances created
        in the 'setUp' method and clears the list.
    """
    instance1 = ""
    instance2 = ""
    instance3 = ""

    @classmethod
    def setUpClass(cls) -> None:
        """
        initializes an empty list to store instances before running the tests.
        """
        cls.instances = []

    @classmethod
    def tearDownClass(cls) -> None:
        """
        clears the list of instances.
        """
        cls.instances.clear()

    def setUp(self) -> None:
        """This method is called b4 each test to set up the initial state."""
        self.instance1 = BaseModel()
        self.instance2 = BaseModel()
        self.instance3 = BaseModel()

    def tearDown(self) -> None:
        del storage.all()["{}.{}".format("BaseModel", self.instance1.id)]
        del storage.all()["{}.{}".format("BaseModel", self.instance2.id)]
        del storage.all()["{}.{}".format("BaseModel", self.instance3.id)]
        self.instances.clear()

    def test__init__(self):
        """
        Tests the proper initialization of 'BaseModel' instances and their
        attributes.
        """
        self.instance1 = BaseModel()
        self.assertIsInstance(self.instance1, BaseModel)
        self.assertIn("id", self.instance1.__dict__.keys())
        self.assertIn("created_at", self.instance1.__dict__.keys())
        self.assertIn("updated_at", self.instance1.__dict__.keys())
        self.assertIsInstance(self.instance1.id, str)
        self.assertIsInstance(self.instance1.created_at, datetime.datetime)
        self.assertIsInstance(self.instance1.updated_at, datetime.datetime)
        self.instance1.name = "My First Model"
        self.instance1.my_number = 89
        self.assertIn("name", self.instance1.__dict__.keys())
        self.assertIn("my_number", self.instance1.__dict__.keys())

    def test__str__(self):
        """Test the str() method returns a correct printed instance format."""
        self.instance1 = BaseModel()
        expected_output = "[BaseModel] ({}) {}".format(
            self.instance1.id, self.instance1.__dict__
            )

    def test_id_uniqueness(self):
        """
        Ensures that the IDs of 'BaseModel' instances are unique.
        """
        self.assertNotEqual(self.instance1.id, self.instance2.id)
        self.assertNotEqual(self.instance2.id, self.instance3.id)
        self.assertNotEqual(self.instance3.id, self.instance1.id)

    def test_save(self):
        """
        Validates that the 'save' method updates the 'updated_at' attribute
        as expected.
        """
        self.instance1 = BaseModel()
        self.instance1.save()
        self.assertNotEqual(
                self.instance1.created_at, self.instance1.updated_at)
        self.assertGreater(
            self.instance1.updated_at, self.instance1.created_at)

    def test_to_dict(self):
        """
        Verifies that the 'to_dict' method returns a dictionary with the
        expected keys and values for 'BaseModel' instances.
        """
        self.instance1 = BaseModel()
        expectedKeys = ["id", "created_at", "updated_at"]
        actualDict = self.instance1.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertTrue((key in list(actualDict)))
        self.assertIsInstance(self.instance1.to_dict(), dict)
        actualDict = self.instance1.to_dict()
        for key in expectedKeys:
            with self.subTest():
                self.assertIsInstance(self.instance1.to_dict()[key], str)
        instance_dict = self.instance1.to_dict()
        self.assertEqual(instance_dict["id"], self.instance1.id)
        self.assertEqual(
            instance_dict["created_at"],
            self.instance1.created_at.isoformat())
        self.assertEqual(
            instance_dict["updated_at"], self.instance1.updated_at.isoformat()
            )
