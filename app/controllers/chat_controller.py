from data.MongoDB_MongoEngine.repository import chat_repository as cr


def initiate_chat(user_1, user_2):
    return cr.initiate_chat()
