from flask_wtf import form

from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore


def get_user_by_email(email):
    return user_datastore.find_user(email=email)


def create_user(first_name, last_name, email, password):
    user_datastore.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password)


