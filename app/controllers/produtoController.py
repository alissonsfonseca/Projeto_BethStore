from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from app.models.tables import Produto, Categoria

produtoController = Blueprint('produtoController', __name__)

@produtoController.route('/produto/cadastro')
@login_required
def cadastroProduto():
    if current_user.admin == True:
        categorias = Categoria.query.all()
        if request.method == 'POST':
            image = request.form.get('image')
            marca = request.form.get('marca')
            modelo = request.form.get('modelo')
            preco = request.form.get('preco')
            tamanho = request.form.get('tamanho')
            quantidade = request.form.get('quantidade')
            categoria = request.form.get('categoria')

            novo_produto = Produto(imagem=image, marca=marca, modelo=modelo,preco=preco, tamanho=tamanho,
            tamanho=tamanho, quantidade=quantidade,id_categoria=categoria)
            db.session.add(novo_produto)
            db.session.commit()
        return render_template('cadastroProduto.html', usuario = current_user, categorias = categorias)
    else:
        return "Acesso apenas para admin"