from fileinput import filename
from flask import Blueprint, Response , render_template, redirect, url_for, request
from flask_login import login_user, login_required, logout_user, current_user
from app import db 
from werkzeug.utils import secure_filename
from app.models.tables import Produto, Categoria, Imagem

produtoController = Blueprint('produtoController', __name__)

@produtoController.route('/produto/cadastro', methods=["GET", "POST"])
@login_required
def cadastroProduto():
    if current_user.admin == True:
        categorias = Categoria.query.all()
        if request.method == 'POST':
            file = request.files['image']
            name = secure_filename(file.filename)
            mimetype = file.mimetype
            imagem = Imagem(img=file.read(), name=name, mimetype=mimetype)
            db.session.add(imagem)
            db.session.commit()
            
            marca = request.form.get('marca')
            modelo = request.form.get('modelo')
            preco = float(request.form.get('preco'))
            tamanho = request.form.get('tamanho')
            quantidade = int(request.form.get('quantidade'))
            categoria = int(request.form.get('categoria'))
            descricao = request.form.get('descricao')
            inf_tecnica = request.form.get('inf_tecnnica')

            novo_produto = Produto(descricao=descricao, inf_tecnica=inf_tecnica, id_categoria=categoria, marca=marca, modelo=modelo,preco=preco, tamanho=tamanho, quantidade=quantidade, id_imagem=imagem.id)
            db.session.add(novo_produto)
            db.session.commit()
            
            
        return render_template('cadastroProduto.html', usuario = current_user, categorias = categorias)
    else:
        return "Acesso apenas para admin"

@produtoController.route('/produtos/<int:id>', methods=['GET','POST'])
def paginaProduto(id):
    produto = Produto.query.get_or_404(id)
    return render_template('produto.html', usuario=current_user, produto=produto)

@produtoController.route('/produtos/imagem/<int:id>', methods=['GET', 'POST'])
def get_imagem(id):
    imagem = Imagem.query.filter_by(id=id).first()
    return Response(imagem.img, mimetype=imagem.mimetype)