#!/usr/bin/python3
""" Module that contain different methods """

from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ definition of class, named (BaseModel)
    """
    def __init__(self):
        """
        The instance of class with public
        instance attributes: id, created_at, updated_at
        """
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """ Returns a string representation of the object
        """
        return ("[{}] ({}) {}".format
                (type(self).__name__, self.id, self.__dict__))

    def save(self):
        """ This method will save the updated_at instance attribute
        """
        self.updated_at = datetime.now()

    def to_dict(self):
        """This set the dictionary aspect of the code
        """
        new_dict = self.__dict__.copy()
        new_dict['__class__'] = type(self).__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()
        return new_dict
