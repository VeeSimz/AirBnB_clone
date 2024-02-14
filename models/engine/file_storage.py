#!/usr/bin/python3
""" Module that uses JSON format to print data """

import json

class FileStorage:
    """ This part defines the class name with methods
    Methods:
        all: returns the objects in dict
        new: assign values to id
        save: save the objects fter serializing
        reload: rload for deserializing
    Class attributes:
        __file_path(str): the path to the file in use
        __objects(str): the object aspect
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """ This returns all the objcet in the dict """
        return self.__objects

    def new(self, obj):
        """ This method set the obj with key <obj class name>.id """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            return self.__objects[key] = obj

    def save(self):
        """ This serializes __objects to the JSON file """
        unit_serializer = {}
        for key,  obj in self.__objects.items():
            unit_serializer[key] = obj.to_dict()
            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                json.dump(unit_serializer, f)

    def reload(self):
        """ This method deserialize the dict objects """
        try:
            with open(self.__file_path, 'w', encoding="UTF-8") as f:
                another_json = json.load(f)
                for key, value in another_json.items():
                    obj = self.class_dict[value['__class__']](**value)
                    self.__objects[key] = obj
                
        except FileNotFoundError:
            pass

