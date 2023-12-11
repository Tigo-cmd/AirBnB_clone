#!/usr/bin/python3
"""
class for place
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    class that inherits from BaseModel
    Attribs:
        name (str): name of the amenity
        city_id: id of the city
        user_id: id of the user
        description: place description
        number_rooms: number of rooms
        number_bathrooms : number of bathroom avaliable
        max_guest: max number of guests
        price_by_night: price of the hotel
        latitude: place cordinates location
        longitude: place cordinates location
        amenity_ids: a list
    """
    def __init__(self, *args, **kwargs):
        """
        class initializer
        """
        super().__init__(*args, **kwargs)
    
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []