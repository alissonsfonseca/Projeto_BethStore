from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager


app = Flask(__name__)
project_dir = os.path.dirname(os.path.abspath(__file__))
database_file = "sqlite:///{}".format(os.path.join(project_dir, "data/database.db"))
app.config["SQLALCHEMY_DATABASE_URI"] = database_file
app.config['SECRET_KEY'] = 'web'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

from app.controllers.controllers import controllers
from app.controllers.autentificador import autentificador
from app.controllers.produtoController import produtoController
from app.controllers.categoriaController import categoriaController

app.register_blueprint(controllers, url_prefix='/')
app.register_blueprint(autentificador, url_prefix='/')
app.register_blueprint(produtoController, url_prefix='/')
app.register_blueprint(categoriaController, url_prefix='/')

from app.models import tables
from app.models.tables import Usuario
db.create_all(app=app)

login_manager = LoginManager()
login_manager.login_view = "autentificador.login"
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return Usuario.query.get(int(id))


