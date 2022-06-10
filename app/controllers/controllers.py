from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models.tables import Imagem, Pedido, Usuario, Produto, Categoria, Aprovacao
from app import db

controllers = Blueprint('controllers', __name__)

@controllers.route('/')
def index():
    produtos = Produto.query.all()
    categorias = Categoria.query.all()
    
    return render_template('index.html', usuario=current_user, produtos=produtos, categorias=categorias)

@controllers.route('/busca', methods = ['POST'])
def busca():
    categorias = Categoria.query.all()
    busca = request.form.get('busca')
    busca = busca.upper()
    categoria = request.form.get("categoria")
    produtos_categoria = db.session.query(Produto).join(Produto.categoria)
    produtos = []
    if busca and categoria == "0":
        for prod in produtos_categoria:
            modelo = str(prod.modelo).upper()
            marca = str(prod.marca).upper()
            categoria = str(prod.categoria.nome).upper()
            if busca in modelo or busca in categoria or busca in marca:
                produtos.append(prod)
    elif not busca and categoria != "0":
        for prod in produtos_categoria:
            if int(categoria) == prod.categoria.id:
                produtos.append(prod)
        categoria = Categoria.query.filter_by(id=categoria).first()
        busca = categoria.nome
    elif busca and categoria != "0":
        for prod in produtos_categoria:
            modelo = str(prod.modelo).upper()
            marca = str(prod.marca).upper()
            if int(categoria) == prod.categoria.id and ((busca in modelo) or (busca in categoria) or (busca in marca)):
                produtos.append(prod)
        categoria = Categoria.query.filter_by(id=categoria).first()
        busca = busca + " em "+ categoria.nome
    else:
        for prod in produtos_categoria:
            produtos.append(prod)
        busca = "todos"
    return render_template('busca.html', usuario=current_user, produtos=produtos, quant = len(produtos), busca = busca, categorias = categorias)

@controllers.route('/dashboard-usuario')
@login_required
def dash_usuario():
    if current_user.admin == True:
        lista_usuario = Usuario.query.all()
        return render_template('dash-user.html', usuario=current_user, lista_usuario = lista_usuario)
    else:
        return 'acesso negado', 400

@controllers.route('/administrador')
@login_required
def administrador():
    if current_user.admin == True:
        return render_template('administrador.html', usuario=current_user)
    else:
        return 'Acesso negado', 400

@controllers.route('/aprovacao', methods=['GET','POST'])
@login_required
def aprovacao():
    if current_user.admin == True:
        pedidos = Pedido.query.all()
        return render_template('aprovacao.html', usuario=current_user, pedidos=pedidos)
    else:
        return 'Acesso negado', 400
    
@controllers.route('/aprovacao/cadastro', methods=['GET','POST'])
@login_required
def cadastrarAprovacao():
    if current_user.admin == True:
        if request.method == 'POST':
            mensagem = request.form.get('mensagem')
            novo_status = Aprovacao(mensagem=mensagem, id_usuario=current_user.id)
        return render_template('cadastroAprovacao.html', usuario=current_user)
    else:
        return 'Acesso negado', 400