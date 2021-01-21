from data.MongoDB_MongoEngine.repository import role_repository as rr


def create_role(name):
    rr.create_role(name)


def get_role_by_name(name):
    return rr.get_role_by_name(name)


def get_all_roles():
    return rr.get_all_roles()


def add_admin_role_to_user(user):
    rr.add_admin_role_to_user(user)


def delete_admin_role_from_user(user):
    rr.delete_admin_role_from_user(user)