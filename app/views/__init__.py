from flask import Flask
from flask_mongoengine import MongoEngine

from data.MongoDB_MongoEngine.db.db_settings import config

app = Flask(__name__)
app.config.from_object(config)
db = MongoEngine(app)

import views.html_routes
import views.api_routes
