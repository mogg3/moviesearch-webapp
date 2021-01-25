from data.MongoDB_MongoEngine.models.chats import Chat
from data.MongoDB_MongoEngine.repository.message_repository import send_message


def initiate_chat(user_1, user_2):
    chat = Chat(members=[user_1, user_2], messages=[])
    chat.save()
    user_1.chats.append(chat)
    user_1.save()
    user_2.chats.append(chat)
    user_2.save()


def get_all_chats():
    return [chat for chat in Chat.objects]


def add_message_to_chat(chat, message):
    chat.messages.append(message)
    chat.save()