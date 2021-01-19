from data.MongoDB_MongoEngine.models.messages import Message
from data.MongoDB_MongoEngine.repository.user_repository import get_user_by_email


def create_message():
    user = get_user_by_email("q@m2123")
    message = Message(sent_by=user, text=f"Hejsan, {user.first_name} här!")
    return message