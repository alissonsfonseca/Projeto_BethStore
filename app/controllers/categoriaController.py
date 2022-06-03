from flask import Blueprint , render_template, redirect, url_for, request
from app import db 
from app.models.tables import Categoria

categoriaController = Blueprint('categoriaController', __name__)

@categoriaController.route('/produto/categoria')
def cadastroCategoria():
        return render_template('cadastroCategoria.html')