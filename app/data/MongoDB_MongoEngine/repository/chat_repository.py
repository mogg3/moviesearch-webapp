from data.MongoDB_MongoEngine.models.chats import Chat
from data.MongoDB_MongoEngine.repository.message_repository import create_message
from data.MongoDB_MongoEngine.repository.user_repository import get_user_by_email


def initiate_chat():
    user1 = get_user_by_email("q@m2123")
    user2 = get_user_by_email("m@m2123")
    message = create_message()
    chat = Chat(members=[user1, user2], messages=[message])
    chat.save()
    return chat

