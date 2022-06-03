from flask import Blueprint , render_template, redirect, url_for, request
from app import db 

produtoController = Blueprint('produtoController', __name__)

@produtoController.route('/produto/cadastro')
def cadastroProduto():
    return render_template('cadastroProduto.html')