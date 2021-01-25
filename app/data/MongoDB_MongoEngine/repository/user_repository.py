from flask_security.utils import hash_password
from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore
from data.MongoDB_MongoEngine.models.users import User


def get_user_by_email(email):
    return user_datastore.find_user(email=email)


def create_user(first_name, last_name, email, password, username):
    user_datastore.create_user(
        first_name=first_name,
        last_name=last_name,
        email=email,
        password=hash_password(password),
        username=username)


def add_role_to_user(user, role):
    user_datastore.add_role_to_user(user=user, role=role)


def get_all_users():
    return [user for user in User.objects]


def get_user_by_username(username):
    return user_datastore.find_user(username=username)


def add_movie_to_users_watchlist(user, movie):
    user.watchlist.append(movie)
    user.save()


def add_friendship(user, friend):
    #TODO Friend invitation
    user.friends.append(friend)
    friend.friends.append(user)
    friend.save()
    user.save()



def delete_movie_from_users_watchlist(user, movie):
    user.watchlist.remove(movie)
    user.save()

def add_profile_picture_to_user(user, profile_picture):
    user.profile_picture.put(profile_picture, content_type='image/jpeg')
    user.save()

def delete_profile_picture_if_exists(user):
    if user.profile_picture:
        user.profile_picture.delete()
    user.save()
