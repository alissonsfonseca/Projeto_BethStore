from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models.tables import Usuario
from app import db
from app.models.tables import Produto 

controllers = Blueprint('controllers', __name__)

@controllers.route('/')
def index():
    produtos = Produto.query.all()
    return render_template('index.html', usuario=current_user, produtos=produtos)


@controllers.route('/dashboard-usuario')
def dash_usuario():
    lista_usuario = Usuario.query.all()
    return render_template('dash-user.html', usuario=current_user, lista_usuario = lista_usuario)
    
