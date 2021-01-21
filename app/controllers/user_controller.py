from data.MongoDB_MongoEngine.repository import user_repository as rm


def get_user_by_email(email: str):
    return rm.get_user_by_email(email)


def get_user_by_username(username: str):
    return rm.get_user_by_username(username)


def create_user(first_name, last_name, email, password, username):
    rm.create_user(first_name, last_name, email, password, username)


def add_role_to_user(user, role):
    rm.add_role_to_user(user=user, role=role)


def get_all_users():
    return rm.get_all_users()


def add_movie_to_users_watchlist(user, movie):
    rm.add_movie_to_users_watchlist(user, movie)


def add_friendship(user, friend):
    rm.add_friendship(user, friend)

def delete_movie_from_users_watchlist(user, movie):
    rm.delete_movie_from_users_watchlist(user, movie)

