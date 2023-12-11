#!/usr/bin/python3
""" class BaseModel that defines all common attributes/methods 
for other classes:
"""

from datetime import datetime
import uuid
import models


class BaseModel:
	"""
	BaseModel that defines all common attributes/methods for other classes
	"""
	def __init__(self, *args, **kwargs):
		"""
		attributes:
			id (str): A unique identifier generated
			created_at (datetime): The timestamp when an instance is created.
			updated_at (datetime): The timestamp when an instance is last
			updated.
		"""
		if kwargs:
		    for i, value in kwargs.items():
			if i != "__class__":
			    if i in ("created_at", "updated_at"):
			        setattr(self, i, datetime.strptime(value,
			                "%Y-%m-%dT%H:%M:%S.%f"))
			    else:
			        setattr(self, i, value)
		else:
		    self.id = str(uuid.uuid4())
		    self.created_at = datetime.now()
		    self.updated_at = datetime.now()
		    models.storage.new(self)

	def __str__(self):
	"""
	return string representation of the class
	"""
	return ("[{}] ({}) ({})".format(self.__class__.__name__,
		self.id, self.__dict__))

	def save(self):
	"""
	Updates the 'updated_at' attribute with the current datetime.
	"""
	self.updated_at = datetime.now()
	models.storage.save()

	def to_dict(self):
	"""
	Returns a dictionary containing all object attributes in a structured
	format for serialization.
	"""
	main = self.__dict__.copy()
	main['__class__'] = self.__class__.__name__
	main['created_at'] = self.created_at.isoformat()
	main['updated_at'] = self.updated_at.isoformat()
	return main
