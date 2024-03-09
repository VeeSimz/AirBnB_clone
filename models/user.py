#!/usr/bin/python3
""" Module that defines class User
"""

from models.base_model import BaseModel
import json


class User(BaseModel):
    """Class User:
    Represents a user in the system, inherits from BaseModel.
    Public Class Attributes:
    - email (str): empty string
    - password (str): empty string
    - first_name (str): empty string
    - last_name (str): empty string
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
