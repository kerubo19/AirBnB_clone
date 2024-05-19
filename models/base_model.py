#!/usr/bin/python3
import uuid
from datetime import datetime


class BaseModel:

    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()  # Record the creation time
        self.updated_at = datetime.now()

    def save(self):
        self.updated_at = datetime.now()  # Update the 'updated_at' timestamp
        # Save the object to the data storage (file, database, etc.)

    def to_dict(self):
        # Convert the object to a dictionary
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
