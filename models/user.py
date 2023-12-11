#!/usr/bin/python3
"""
a class User that inherits from BaseModel:
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    this class inherits from basemodel
    attrib:
        email (str): user email
        password (str): user pasword
        first_name (str): user first name
        last_name (str) user last name
    """
    email = ""
    password  = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """
        class initializer
        """
        super().__init__(*args, **kwargs)