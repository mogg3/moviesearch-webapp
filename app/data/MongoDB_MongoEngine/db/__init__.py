from flask_mongoengine import MongoEngine

from views import app

db = MongoEngine(app)
