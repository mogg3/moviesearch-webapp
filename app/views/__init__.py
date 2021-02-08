from flask import Flask
from flask_cors import CORS

from data.MongoDB_MongoEngine.db_settings import config

app = Flask(__name__)
CORS(app)
app.config.from_object(config)

import views.html_routes
import views.api_routes

from views.html_routes import index

app.register_blueprint(index)