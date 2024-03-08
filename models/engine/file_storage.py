#!/usr/bin/python3
'''This is a module named File Storage'''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """ This is a storage engine to store objects in json file
    Class Methods:
        all: Returns the dictionary object
        new: updates the dictionary with class name and id
        save: Serializes python objects into JSON strings
        reload: Deserializes, or converts JSON strings into key and val
    Class Attributes:
        __file_path (str): The name of the json file
        __objects (dict): A dictionary of created instantiated objects.
        class_init (dict): A dictionary of all the classes.
    """

    __file_path = 'file.json'
    __objects = {}
    __class_init = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "Amenity": Amenity,
            "City": City,
            "Review": Review,
            "State": State
            }

    def all(self):
        '''Return dictionary of <class>.<id> : object instance'''
        return self.__objects

    def new(self, obj):
        '''Set new __objects to existing dictionary of instances'''
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Save/serialize obj dictionaries to json file"""
        my_dict = {}

        for key, obj in self.__objects.items():
            my_dict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def reload(self):
        """Deserialize/convert obj dicts back to instances, if it exists"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                fine_dict = json.load(f)
            for key, value in fine_dict.items():
                obj = self.__class_init[value['__class__']](**value)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
