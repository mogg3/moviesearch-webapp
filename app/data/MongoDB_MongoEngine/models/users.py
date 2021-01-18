from flask_security import UserMixin

from data.MongoDB_MongoEngine.models.roles import Role
from views import db


class User(db.Document, UserMixin):
    first_name = db.StringField(max_length=40)
    last_name = db.StringField(max_length=40)
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role))
    watchlist = db.ListField(default=[])

    def __str__(self):
        return self.first_name