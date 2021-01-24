from mongoengine import EmbeddedDocument, ReferenceField, StringField, DateTimeField
import datetime


class Message(EmbeddedDocument):
    sent_by = ReferenceField('User')
    text = StringField(max_length=500)
    created_at = DateTimeField(default=datetime.datetime.now)

