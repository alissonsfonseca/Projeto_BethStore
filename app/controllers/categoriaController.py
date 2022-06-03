from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from app.models.tables import Categoria

categoriaController = Blueprint('categoriaController', __name__)

@categoriaController.route('/produto/categoria')
@login_required
def cadastroCategoria():
        if current_user.admin == True:
                return render_template('cadastroCategoria.html')
        else:
                return 'Acesso exclusivo de administrador'

        