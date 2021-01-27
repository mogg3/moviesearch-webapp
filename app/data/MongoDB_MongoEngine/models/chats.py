from mongoengine import ListField, Document, EmbeddedDocumentListField, ReferenceField


class Chat(Document):
    members = ListField(ReferenceField('User'))
    messages = EmbeddedDocumentListField('Message')

