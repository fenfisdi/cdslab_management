from mongoengine import (BooleanField, StringField)

from .base import BaseDocument


class Template(BaseDocument):
    name = StringField()
    content = StringField()
    is_enabled: BooleanField(default=True)
