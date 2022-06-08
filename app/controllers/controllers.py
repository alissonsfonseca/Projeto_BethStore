from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app.models.tables import Imagem, Usuario, Produto, Categoria
from app import db

controllers = Blueprint('controllers', __name__)

@controllers.route('/')
def index():
    produtos = Produto.query.all()
    categorias = Categoria.query.all()

    return render_template('index.html', usuario=current_user, produtos=produtos, categorias=categorias)

@controllers.route('/busca', methods = ['POST'])
def busca():
    busca = request.form.get('busca')
    if busca:
        produtos = Produto.query.filter(Produto.marca.contains(busca) | Produto.modelo.contains(busca))
        quant = 0
        for produto in produtos:
            quant = quant + 1
    return render_template('busca.html', usuario=current_user, produtos=produtos, quant=quant, busca=busca)

@controllers.route('/dashboard-usuario')
def dash_usuario():
    lista_usuario = Usuario.query.all()
    return render_template('dash-user.html', usuario=current_user, lista_usuario = lista_usuario)
    
