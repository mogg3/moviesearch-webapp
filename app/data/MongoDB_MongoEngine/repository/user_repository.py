from flask_wtf import form

from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore
from data.MongoDB_MongoEngine.models.users import User
from views import db

def get_user_by_email(email):
    return user_datastore.find_user(email=email)


def create_user(first_name, last_name, email, password, username):
    user_datastore.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=password,
        username=username)


def add_role_to_user(user, role):
    user_datastore.add_role_to_user(user=user, role=role)


def get_all_users():
    users = []
    for user in User.objects:
        users.append(user)
    return users


def get_user_by_username(username):
    return user_datastore.find_user(username=username)