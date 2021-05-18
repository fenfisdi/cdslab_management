from mongoengine import (
    Document, 
    StringField, 
    BooleanField)

class Template(Document):
    name = StringField()
    content = StringField()
    is_enabled: BooleanField(default=True)