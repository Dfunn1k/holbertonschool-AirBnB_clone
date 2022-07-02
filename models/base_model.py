#!/usr/bin/python3
"""BaseModel Class implementation"""
from datetime import datetime
import uuid
import models


class BaseModel():
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Initial instance"""
        if not kwargs:
            self.id = str(uuid.uuid4())
            self.updated_at = datetime.now()
            self.created_at = datetime.now()
            models.storage.new(self)

        else:
            new_dict = {}
            for key, value in kwargs.items():
                if key == 'created_at' or key == 'updated_at':
                    new_dict[key] = datetime.fromisoformat(value)
                elif key != '__class__':
                    new_dict[key] = value
            self.__dict__.update(new_dict)

    def __str__(self):
        """String representation of the instance"""
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Save a dict representation of the instance into a file"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the instance to a dict representation"""
        instance_dict = self.__dict__
        new_dict = {}
        new_dict["__class__"] = type(self).__name__
        for key, value in instance_dict.items():
            if key == 'created_at' or key == 'updated_at':
                new_dict[key] = value.isoformat()
            else:
                new_dict[key] = value

        return new_dict
