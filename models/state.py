#!/usr/bin/python3
"""
class for state
"""

from models.base_model import BaseModel


class State(BaseModel):
    """
    class that inherits from BaseModel
    Attribs:
        name (str): name of the state
    """
    def __init__(self, *args, **kwargs):
        """
        class initializer
        """
        super().__init__(*args, **kwargs)
    
    name = ""