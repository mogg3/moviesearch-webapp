from flask import Flask
from flask_mongoengine import MongoEngine
#from flask_cors import CORS
from data.MongoDB_MongoEngine.db.db_settings import config

app = Flask(__name__)
#CORS(app)
app.config.from_object(config)
db = MongoEngine(app)

import views.html_routes
import views.api_routes
