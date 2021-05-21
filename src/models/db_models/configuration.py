from mongoengine import (IntField)

from .base import BaseDocument


class Configuration(BaseDocument):
    storage_time = IntField(min_value=1)
    simulation_removal_before = IntField(min_value=1)
    simulation_scheduled_removal = IntField(min_value=1)
