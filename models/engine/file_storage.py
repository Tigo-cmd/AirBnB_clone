#!/usr/bin/env python3
"""
serializes instances to a JSON file and deserializes JSON file to instances:
"""

import json
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from models.base_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and deserializes JSON file to instances:
    initializes private attribtes for the class
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
         returns the dictionary __objects
         """
         return self.__objects
    
    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        key = "{}.{}".format(type(obj).__name__, obj.id)
        pair = obj
        self.__objects[key] = pair
    
    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        dict_obj = {}
        for i, value in self.__objects.items():
            dict_obj[i] = value.to_dict()
        with open(self.__file_path, "w", encoding="utf-8") as file:
            json.dump(dict_obj, file)
        
    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file 
        (__file_path) exists ; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised)
        """
        classes = {
            'BaseModel': BaseModel,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Place': Place,
            'Review': Review,
        }
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                from_json = json.load(f)
                if from_json is None: 
                    pass
                else:
                    for i, value in from_json.items():
                        name = value['__class__']
                        if name in classes:
                            instance_class = classes[name]
                            instance = instance_class(**value)
                            self.__objects[i] = instance
        except FileNotFoundError:
            pass