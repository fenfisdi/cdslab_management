from mongoengine import (BooleanField, StringField)

from .base import BaseDocument


class Template(BaseDocument):
    name = StringField(default="Default")
    content = StringField(default="<html></html>")
    is_enabled: BooleanField(default=True)
