from data.MongoDB_MongoEngine.models.messages import Message


def send_message(sent_by, text):
    return Message(sent_by=sent_by, text=f"{sent_by.username}: {text}")
