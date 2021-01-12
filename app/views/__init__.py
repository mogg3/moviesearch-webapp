from flask import Flask
from flask_mongoengine import MongoEngine
from flask_security import MongoEngineUserDatastore, \
    UserMixin, RoleMixin, Security, roles_required

app = Flask(__name__)

app.config['MONGODB_SETTINGS'] = {
    'connect': False,
    'host': "mongodb://root:s3cr37@localhost:27028/movie_web_app?authSource=admin"
}

app.secret_key = 'super secret key'
db = MongoEngine(app)
app.config['SECURITY_PASSWORD_SALT'] = 'lkjsdflkilkjsdlkjndlkk'

class Role(db.Document, RoleMixin):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(db.Document, UserMixin):
    first_name = db.StringField(max_length=40)
    last_name = db.StringField(max_length=40)
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField()
    roles = db.ListField(db.ReferenceField(Role), default=[])

    def __str__(self):
        print(self.first_name)
        print(self.last_name)
        print(self.email)
        print(self.password)

user_datastore = MongoEngineUserDatastore(db, User, Role)
security = Security(app, user_datastore)

import views.html_routes
import views.api_routes
