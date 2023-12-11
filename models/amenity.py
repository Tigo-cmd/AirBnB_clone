#!/usr/bin/python3
"""
class for Amenity
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    class that inherits from BaseModel
    Attribs:
        name (str): name of the amenity
    """
    def __init__(self, *args, **kwargs):
        """
        class initializer
        """
        super().__init__(*args, **kwargs)