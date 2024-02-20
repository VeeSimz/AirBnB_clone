#!/usr/bin/python3
""" Module that contain different methods used """
import models
from uuid import uuid4
from datetime import datetime


class BaseModel():
    """ definition of class, named (BaseModel)

    Methods:
    __init__(args, kwargs)
    save(self)
    __repr__(self)
    __str(self)__
    """

    def __init__(self, *args, **kwargs):
        """
        The instance of class with public
        instance attributes: id, created_at, updated_at
        """
        date_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime
                    (kwargs["created_at"], date_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime
                    (kwargs["updated_at"], date_format)
                elif "__class__" == key:
                    pass
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """ Returns a string representation of the object
        """
        return ("[{}] ({}) {}".format
                (self.__class__.__name__, self.id, self.__dict__))

        def __repr__(self):
            """
            return the official string representaion
            """
            return (self.__str__())

    def save(self):
        """ This method will save the updated_at instance attribute
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """This set the dictionary aspect of the code
        """
        new_dict = self.__dict__.copy()
        new_dict["__class__"] = self.__class__.__name__
        new_dict["created_at"] = self.created_at.isoformat()
        new_dict["updated_at"] = self.updated_at.isoformat()

        return new_dict
