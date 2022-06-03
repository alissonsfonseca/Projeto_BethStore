from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from app.models.tables import Categoria

categoriaController = Blueprint('categoriaController', __name__)

@categoriaController.route('/produto/categoria', methods=['GET', 'POST'])
@login_required
def cadastroCategoria():
        if current_user.admin == True:
                if request.method == 'POST':
                        nome = request.form.get('nome')
                        setor = request.form.get('setor')
                        descricao = request.form.get('descricao')

                        categoria_nova = Categoria(nome=nome, setor=setor, descricao=descricao)
                        db.session.add(categoria_nova)
                        db.session.commit()
                return render_template('cadastroCategoria.html', usuario = current_user)
        else:
                return 'Acesso exclusivo de administrador'

        