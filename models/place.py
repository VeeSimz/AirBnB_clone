#!/usr/bin/python3
"""
Place class, a subclass module of BaseModel class
"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    A subclass of BaseModel class
    Public class attributes:
        city_id(str): will be City.id
        user_id(str): will be User.id
        name(str): a string
        description(str): accept a string
        number_rooms(int): 0 will be initialized
        number_bathrooms(int): 0 will be initialized
        max_guest(int): 0 will be initialized
        price_by_night(int): 0 will be initialized
        latitude(float): 0.0 will be initialized
        longitude(float:) 0.0 will be initialzed value
        amenity_ids(list): will be Amenity.id
    """
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
