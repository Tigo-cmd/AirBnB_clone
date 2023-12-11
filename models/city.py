#!/usr/bin/python3
"""
class for City
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    class that inherits from BaseModel
    Attribs:
        name (str): name of the city
        state_id (str): id of the state where the city is located
    """
    def __init__(self, *args, **kwargs):
        """
        class initializer
        """
        super().__init__(*args, **kwargs)
    
    state_id = ""
    name = ""