from app import db
from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import login_required, current_user
from app.models.tables import Carrinho, Cliente, Produto, Usuario


carrinhoController = Blueprint('carrinhoController', __name__)

@carrinhoController.route("/carrinho", methods=["GET", "POST"])
@login_required
def carrinho():
    cliente = Cliente.query.filter_by(id_usuario=current_user.id).first()
    id = cliente.id
    carrinho = Carrinho.query.filter_by(id_cliente=id)
    return render_template("carrinho.html", usuario = current_user, carrinho=carrinho)

@carrinhoController.route("/carrinho/produto/<int:id>", methods=["GET", "POST"])
@login_required
def produtoCarrinho(id):
    cliente = Cliente.query.filter_by(id_usuario=current_user.id).first()
    id_cliente = cliente.id
    id_produto = id
    valor_frete = 10.0
    previsao_entrega = 3
    carrinho = Carrinho(id_cliente=id_cliente, id_produto=id_produto, valor_frete=valor_frete, previsao_entrega=previsao_entrega)
    db.session.add(carrinho)
    db.session.commit()
    return redirect("/carrinho")