#!/usr/bin/python3
'''
This module defines the base model class
'''
import uuid
from datetime import datetime


class BaseModel:
    '''
    Base class for other classes
    '''
    def __init__(self):
        '''
        intialize public attributes
        '''
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()  # Record the creation time
        self.updated_at = datetime.now()

    def save(self):
        '''
        update  the updated at
        '''
        self.updated_at = datetime.now()

    def to_dict(self):
        '''
        Return dictionary presentation
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        '''
        Return strin presentation
        '''
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)
