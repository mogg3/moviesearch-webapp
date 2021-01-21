from data.MongoDB_MongoEngine.db.db_user_role_security import user_datastore
from data.MongoDB_MongoEngine.models.roles import Role


def create_role(name):
    user_datastore.create_role(name=name)


def get_role_by_name(name):
    return user_datastore.find_role(name)


def get_all_roles():
    return [role for role in Role.objects]


def add_admin_role_to_user(user):
    user_datastore.add_role_to_user(name='admin')


def delete_admin_role_from_user(user):
    user_datastore.remove_role_from_user(user, user.role['admin'])