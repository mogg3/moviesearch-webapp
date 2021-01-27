from flask_security import RoleMixin

from mongoengine import StringField, Document


class Role(Document, RoleMixin):
    name = StringField(max_length=80, unique=True)
    description = StringField(max_length=255)

    def __str__(self):
        return self.name
