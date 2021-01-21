from flask_security import UserMixin
from mongoengine import StringField, Document, BooleanField, DateTimeField, ListField, ReferenceField, FileField, \
    ImageField


class User(Document, UserMixin):
    first_name = StringField(max_length=40)
    last_name = StringField(max_length=40)
    email = StringField(max_length=100, unique=True)
    username = StringField(max_length=50, unique=True)
    password = StringField(max_length=255)
    active = BooleanField(default=True)
    confirmed_at = DateTimeField(nullable=True)
    watchlist = ListField()
    friends = ListField(ReferenceField('User'))
    roles = ListField(ReferenceField('Role'))
    chats = ListField(ReferenceField('Chat'))
    profile_picture = FileField()

    def __str__(self):
        return f"{self.first_name}"


