from flask_security import RoleMixin

from views import db


class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)

    def __repr__(self):
        return self.name
