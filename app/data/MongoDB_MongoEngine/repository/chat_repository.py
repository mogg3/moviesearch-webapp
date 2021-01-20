from data.MongoDB_MongoEngine.models.chats import Chat
from data.MongoDB_MongoEngine.repository.message_repository import send_message


def initiate_chat(user_1, user_2):
    chat = Chat(members=[user_1, user_2], messages=[send_message()])
    chat.save()
    print(chat)
