from data.MongoDB_MongoEngine.repository import role_repository as rr


def create_role(name):
    rr.create_role(name)

def get_role_by_name(name):
    return rr.get_role_by_name(name)