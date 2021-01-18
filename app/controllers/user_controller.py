from data.MongoDB_MongoEngine.repository import user_repository as rm


def get_user_by_email(email: str):
    return rm.get_user_by_email(email)


def create_user(first_name, last_name, email, password):
    rm.create_user(first_name, last_name, email, password)