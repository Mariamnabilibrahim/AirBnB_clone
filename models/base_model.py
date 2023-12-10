#!/usr/bin/python3
"""Function defines all common methods for other classes."""
import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """BaseModel of the HBnB project."""

    def __init__(self, *args, **kwargs):
        """Arguments for the constructor."""
        tform = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        if len(kwargs) != 0:
            for x, y in kwargs.items():
                if x == "created_at" or x == "updated_at":
                    self.__dict__[x] = datetime.strptime(y, tform)
                else:
                    self.__dict__[x] = y
        else:
            models.storage.new(self)

    def save(self):
       """Updates the public instance attribut,
       updated_at with the current datetime.
       """
       self.updated_at = datetime.today()
       models.storage.save()

    def to_dict(self):
        """Returns a dictionary containing,
        all keys/values of __dict__ of the instance.
        """
        rdict = self.__dict__.copy()
        rdict["created_at"] = self.created_at.isoformat()
        rdict["updated_at"] = self.updated_at.isoformat()
        rdict["__class__"] = self.__class__.__name__
        return rdict

    def __str__(self):
        """Representation of the BaseModel instance."""
        clname = self.__class__.__name__
        return "[{}] ({}) {}".format(clname, self.id, self.__dict__)
