from mongoengine import EmbeddedDocument, ReferenceField, StringField


class Message(EmbeddedDocument):
    sent_by = ReferenceField('User')
    text = StringField(max_length=500)

    def __str__(self):
        return f"'{self.text}' (sent by {self.sent_by.first_name}"
