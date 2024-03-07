#!/usr/bin/python3
""" Module that defines class named BaseModel in AiBnB project """
from datetime import datetime
from uuid import uuid4
import models


class BaseModel():
    """ BaseModel class for the AirBnB clone project.
    Attributes:
    None

    Methods:
        __init__(self, *args, **kwargs)
        __str__(self)
        __save(self)
        __repr__(self)
        to_dict(self)
    """

    def __init__(self, *args, **kwargs):
        """ Initialize a new BaseModel instance.

        Args:
            args: Variable arguments.
            kwargs: Keyword arguments with instance attributes.

        Attributes:
            id (str): A unique identifier for each instance.
            created_at (datetime): The date and time when it is created.
            updated_at (datetime): The date and time it is updated.
        """
        data_format = '%Y-%m-%dT%H:%M:%S.%f'
        if kwargs:
            for key, value in kwargs.items():
                if "created_at" == key:
                    self.created_at = datetime.strptime(kwargs["created_at"],
                                                        data_format)
                elif "updated_at" == key:
                    self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                        data_format)
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
        """
        Return class name, id, and the dictionary
        """
        return ('[{}] ({}) {}'.
                format(self.__class__.__name__, self.id, self.__dict__))

    def __repr__(self):
        """
        returns string repr
        """
        return (self.__str__())

    def save(self):
        """
        Instance method to:
        - update current datetime
        - invoke save() function &
        - save to serialized file
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Return dictionary of BaseModel with string formats of times
        """
        print_dic = self.__dict__.copy()
        print_dic["created_at"] = self.created_at.isoformat()
        print_dic["updated_at"] = self.updated_at.isoformat()
        print_dic["__class__"] = self.__class__.__name__
        return print_dic
