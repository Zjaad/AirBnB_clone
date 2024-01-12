#!/usr/bin/python3
""" This module represente all classes of the project. """
import uuid
from datetime import datetime


class BaseModel:
    """ the basemodel class. """
    def __init__(self, *args, **kwargs):
        """ initializitaion of new Basemodel inst. """
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    setattr(self, k, datetime.fromisoformat(v))
                elif k != "__class__":
                    setattr(self, k, v)
    def save(self):
        """ updates the public inst attribute update_at. """
        self.updated_at = datetime.now()

    def to_dict(self):
        """ it returns a dictionary that 
        contains all keys n' values of __dict__of. """
        d = self.__dict__.copy()
        d['created_at'] = self.created_at.isoformat()
        d['updated_at'] = self.updated_at.isoformat()
        d['__class__'] = self.__class__.__name__
        return (d)

    def __str__(self):
        """ turning obj to str. """
        return ("[{}] ({}) {}".format(
                self.__class__.__name__, self.id, self.__dict__
        ))


