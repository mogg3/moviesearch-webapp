from mongoengine import ListField, Document, EmbeddedDocumentListField, ReferenceField


class Chat(Document):
    members = ListField(ReferenceField('User'))
    messages = EmbeddedDocumentListField('Message')


    def __str__(self):
        return f"Members = {self.members} Messages={self.messages}"

