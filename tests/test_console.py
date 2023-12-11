#!/usr/bin/python3
"""defines unit tests for the HBNBCommand class."""

import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class Test_HBNBCommand(unittest.TestCase):
	def test_prompt(self):
		"""Test  '(hbnb) '."""
		self.assertEqual("(hbnb)", HBNBCommand.prompt)

	def test_create(self):
		"""
		Test method.

		"""
		input = "create"
		expected_output = "** class name missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output, output)
		input = "create invalidClass"
		expected_output = "** class doesn't exist **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output, output)
		input = "create BaseModel"
		expected_regex = "........-....-....-....-............"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input)
		    output = fakeOutput.getvalue().strip()
		    self.assertRegex(output, expected_regex)

	def test_exit(self):
		"""
		Test exit method.
		    Test "quit" command.
		    Test  "EOF" command.
		"""
		input = "quit"
		expected_output = True
		result = HBNBCommand().onecmd(input)
		self.assertEqual(result, expected_output)
		with patch("builtins.input", side_effect=["quit"]):
		    self.assertTrue(HBNBCommand().onecmd("quit"))

		input = "EOF"
		expected_output = True
		result = HBNBCommand().onecmd(input)
		self.assertEqual(result, expected_output)

		with patch("builtins.print") as mock_print:
		    with patch("builtins.input", side_effect=["EOF"]):
			self.assertTrue(HBNBCommand().onecmd("EOF"))
			mock_print.assert_called_with()

	def test_empty_line(self):
		""" test empty line
		"""

		input = "   \n\t  \r\n     \n\t  \
		\r\n"
		expected_output = ""
		with patch("sys.stdout", new=StringIO()) as fakeOut:
		    HBNBCommand().onecmd(input)
		    output = fakeOut.getvalue().strip("\n")
		    self.assertEqual(expected_output, output)
		with patch("builtins.print") as mock_print:
		    cmd = HBNBCommand()
		    cmd.emptyline()
		    mock_print.assert_not_called()

	def test_show(self):
		"""
		Test show method.
		This method tests the 'show' command in the HBNBCommand class.
		It verifies the behavior when
		    the class name is missing,
		    when the class doesn't exist,
		    when the instance ID is missing, and
		    whenno instance is found.
		"""
		input1 = "show"
		expected_output1 = "** class name missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input1)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input2 = "show InvalidClass"
		expected_output1 = "** class doesn't exist **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input2)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input3 = "show BaseModel"
		expected_output1 = "** instance id missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input3)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input4 = "show BaseModel InvalidId"
		expected_output1 = "** no instance found **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input4)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

	def test_destroy(self):
		"""
		Test destroy method.
		This method tests the 'destroy' command in the HBNBCommand class.
		It verifies the behavior
		    when the class name is missing,
		    when the class doesn't exist,
		    when the instance ID is missing, and
		    when no instance is found.
		"""
		input1 = "destroy"
		expected_output1 = "** class name missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input1)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input2 = "destroy InvalidClass"
		expected_output1 = "** class doesn't exist **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input2)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input3 = "destroy BaseModel"
		expected_output1 = "** instance id missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input3)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input4 = "destroy BaseModel InvalidId"
		expected_output1 = "** no instance found **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input4)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

	def test_all(self):
		"""
		Test all method.
		This method tests the 'all' command in the HBNBCommand class.
		it verifies the behavior when the class doesn't exist.
		"""
		input2 = "all InvalidClass"
		expected_output1 = "** class doesn't exist **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input2)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

	def test_count(self):
		"""
		Test count method.
		This method tests the 'count' command in the HBNBCommand class.
		It verifies the behavior when the class name is missing and
		when the class doesn't exist.
		"""
		input1 = "count"
		expected_output1 = "** class name missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input1)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input2 = "count InvalidClass"
		expected_output1 = "** class doesn't exist **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input2)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

	def test_update(self):
		"""
		test update method when:
		    class name missing
		    class doesn't exist
		    update BaseModel InvalidId
		    instance id missing

		"""
		input1 = "update"
		expected_output1 = "** class name missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input1)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input2 = "update InvalidClass"
		expected_output1 = "** class doesn't exist **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input2)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input3 = "update BaseModel"
		expected_output1 = "** instance id missing **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input3)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

		input4 = "update BaseModel InvalidId"
		expected_output1 = "** no instance found **"
		with patch("sys.stdout", new=StringIO()) as fakeOutput:
		    HBNBCommand().onecmd(input4)
		    output = fakeOutput.getvalue().strip()
		    self.assertEqual(expected_output1, output)

	def test_default(self):
		"""
		test the default value return
		"""
		input1 = "InvalidInput"
		expected_output1 = "** Unknown syntax: {}".format(input1)
		with patch("sys.stdout", new=StringIO()) as fakeError:
		    HBNBCommand().onecmd(input1)
		    error = fakeError.getvalue().strip()
		    self.assertEqual(error, expected_output1)
