from flask import Flask
from flask_cors import CORS
from flask_wtf.csrf import CSRFProtect
from data.MongoDB_MongoEngine.db_settings import config

app = Flask(__name__)
CORS(app)
app.config.from_object(config)

# csrf = CSRFProtect()
# csrf.init_app(app)

import views.html_routes
import views.api_routes
