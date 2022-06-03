from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from app.models.tables import Produto, Categoria

produtoController = Blueprint('produtoController', __name__)

@produtoController.route('/produto/cadastro', methods=["GET", "POST"])
@login_required
def cadastroProduto():
    if current_user.admin == True:
        categorias = Categoria.query.all()
        if request.method == 'POST':
            #image = request.form.get('image')
            marca = request.form.get('marca')
            modelo = request.form.get('modelo')
            preco = float(request.form.get('preco'))
            tamanho = request.form.get('tamanho')
            quantidade = int(request.form.get('quantidade'))
            categoria = int(request.form.get('categoria'))

            novo_produto = Produto(id_categoria=categoria, marca=marca, modelo=modelo,preco=preco, tamanho=tamanho, quantidade=quantidade)
            db.session.add(novo_produto)
            db.session.commit()
        return render_template('cadastroProduto.html', usuario = current_user, categorias = categorias)
    else:
        return "Acesso apenas para admin"