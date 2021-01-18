from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore


def create_role(name):
    user_datastore.create_role(name=name)

def get_role_by_name(name):
    return user_datastore.find_role(name)