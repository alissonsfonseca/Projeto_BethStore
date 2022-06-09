from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from app.models.tables import Categoria, Setor

categoriaController = Blueprint('categoriaController', __name__)

@categoriaController.route('/produto/categoria', methods=['GET', 'POST'])
@login_required
def cadastroCategoria():
        setores = Setor.query.all()
        if current_user.admin == True:
                if request.method == 'POST':
                        nome = request.form.get('nome')
                        setor = request.form.get('setor')
                        descricao = request.form.get('descricao')

                        categoria_nova = Categoria(nome=nome, id_setor=setor, descricao=descricao)
                        db.session.add(categoria_nova)
                        db.session.commit()
                return render_template('cadastroCategoria.html', usuario = current_user, setores=setores)
        else:
                return 'Acesso exclusivo de administrador'

@categoriaController.route('/produto/categoria/catalogo', methods=['GET', 'POST'])
@login_required
def catalogoCategoria():
        categorias = Categoria.query.all()
        return render_template('catalogoCategoria.html', usuario=current_user, categorias=categorias)     