from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager

app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data/database.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from app.controllers.controllers import controllers
from app.controllers.autentificador import autentificador

app.register_blueprint(controllers, url_prefix='/')
app.register_blueprint(autentificador, url_prefix='/')

from app.models import tables
db.create_all()

login_manager = LoginManager()
login_manager.login_view = 'autentificador.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return tables.Usuario.query.get(int(id))

