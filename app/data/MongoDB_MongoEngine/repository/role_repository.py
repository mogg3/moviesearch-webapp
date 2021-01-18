from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore
from data.MongoDB_MongoEngine.models.roles import Role


def create_role(name):
    user_datastore.create_role(name=name)


def get_role_by_name(name):
    return user_datastore.find_role(name)


def get_all_roles():
    roles = []
    for role in Role.objects:
        roles.append(role)
    return roles
