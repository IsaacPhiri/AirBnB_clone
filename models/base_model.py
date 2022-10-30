#!/usr/bin/python3
"""
This module contains a class BaseModel
that defines all common attributes/methods for other classes
"""

import models
from datetime import datetime
import uuid

date_format = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:
    """
    Implementation of BaseModel class
    """
    def __init__(self, *args, **kwargs):
<<<<<<< HEAD
        """
        Initialization of the class
        """
        if not kwargs:
            self.id = str(uuid.uuid4())
=======
        """this is a public class attribute"""
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                elif key == 'updated_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                elif key == 'created_at':
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                if 'id' not in kwargs.keys():
                    self.id = str(uuid4())
                if 'created_at' not in kwargs.keys():
                    self.created_at = datetime.now()
                if 'updated_at' not in kwargs.keys():
                    self.updated_at = datetime.now()
                setattr(self, key, value)

        else:
            self.id = str(uuid4())
>>>>>>> 41ee7fbc2e9413156d2c01c717d639f0fe183dbf
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)
            return

        for key, value in kwargs.items():
            if key != "__class__":
                setattr(self, key, value)
        if hasattr(self, "created_at") and type(self.created_at) is str:
            self.created_at = datetime.strptime(kwargs["created_at"],
                                                date_format)
        if hasattr(self, "updated_at") and type(self.updated_at) is str:
            self.updated_at = datetime.strptime(kwargs["updated_at"],
                                                date_format)

    def __str__(self):
        """
        String representation of the class
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """
        updates the public instance attribute updated_at with the
        current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary containing all keys/values of __dict__
        of the instance
        """
        ndict = self.__dict__.copy()
        ndict["__class__"] = self.__class__.__name__
        ndict["created_at"] = datetime.isoformat(self.created_at)
        ndict["updated_at"] = datetime.isoformat(self.updated_at)
        return ndict
