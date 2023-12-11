#!/usr/bin/python3
"""
class for review
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    class that inherits from BaseModel
    Attribs:
       user_id: id of the user
       place_id: id of the place
       text: content reviewed
    """
    def __init__(self, *args, **kwargs):
        """
        class initializer
        """
        super().__init__(*args, **kwargs)
    
    place_id = ""
    user_id = ""
    text = ""