from data.MongoDB_MongoEngine.models.chats import Chat


def initiate_chat(user_1, user_2):
    chat = Chat(members=[user_1, user_2], messages=[])
    chat.save()
    user_1.chats.append(chat)
    user_1.save()
    user_2.chats.append(chat)
    user_2.save()


def get_all_chats():
    return [chat for chat in Chat.objects]


def get_chat_between_users(user1, user2):
    for chat in Chat.objects:
        if user1 and user2 in chat.members:
            return chat


def add_message_to_chat(chat, message):
    chat.messages.append(message)
    chat.save()