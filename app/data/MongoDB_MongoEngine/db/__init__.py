from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore, Security
from mongoengine import PULL, CASCADE

from data.MongoDB_MongoEngine.models.roles import Role
from data.MongoDB_MongoEngine.models.users import User
from data.MongoDB_MongoEngine.models.messages import Message
from data.MongoDB_MongoEngine.models.chats import Chat
from views import app

db = MongoEngine(app)

from data.MongoDB_MongoEngine.db import db

# User.register_delete_rule(Chat, "chats", PULL)

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)



