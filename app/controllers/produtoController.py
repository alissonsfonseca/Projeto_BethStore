from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from app.models.tables import Produto

produtoController = Blueprint('produtoController', __name__)

@produtoController.route('/produto/cadastro')
@login_required
def cadastroProduto():
    if current_user.admin == True:
        return render_template('cadastroProduto.html', usuario = current_user)
    else:
        return "Acesso apenas para admin"