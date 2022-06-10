from app import db
from flask import Blueprint, redirect, render_template, request, session, url_for
from flask_login import login_required, current_user
from app.models.tables import Carrinho, Categoria, Cliente, Pedido, Produto, Usuario, ProdutoPedido


carrinhoController = Blueprint('carrinhoController', __name__)

@carrinhoController.route("/carrinho", methods=["GET", "POST"])
@login_required
def carrinho():
    categorias = Categoria.query.all()
    cliente = Cliente.query.filter_by(id_usuario=current_user.id).first()
    id = cliente.id
    carrinho = Carrinho.query.filter_by(id_cliente=id)
    item = Carrinho.query.filter_by(id_cliente=id).first()
    if item:
        valor = item.valor_frete
    else:
        valor = 0
    total = 0
    for items in carrinho:
        total = total + (items.produto.preco * items.quantidade)
    return render_template("carrinho.html", usuario = current_user, carrinho=carrinho, categorias=categorias, frete = valor, total = total, cliente=cliente)
        

@carrinhoController.route("/carrinho/produto/<int:id>/<int:quant>", methods=["GET", "POST"])
@login_required
def produtoCarrinho(id, quant):
    cliente = Cliente.query.filter_by(id_usuario=current_user.id).first()
    id_cliente = cliente.id
    id_produto = id
    valor_frete = 10.0
    previsao_entrega = 3
    quantidade = quant
    carrinho = Carrinho(id_cliente=id_cliente, id_produto=id_produto, valor_frete=valor_frete, previsao_entrega=previsao_entrega, quantidade = quantidade)
    db.session.add(carrinho)
    db.session.commit()
    return redirect(url_for("carrinhoController.carrinho"))

@carrinhoController.route("/carrinho/finalizar", methods=['POST'])
@login_required
def finalizarCarrinho():
    if request.method == 'POST':
        cliente = Cliente.query.filter_by(id_usuario=current_user.id).first()
        id = cliente.id
        carrinho = Carrinho.query.filter_by(id_cliente=id)
        pagamento = request.form.get('pagamento')
        total = 0
        for items in carrinho:
            total = total + (items.produto.preco * items.quantidade)
        valor = 10

        novo_pedido = Pedido(valor_frete=10, previsao_entrega=0, forma_pagamento=pagamento,pagamento=0,total=total, id_cliente=cliente.id)
        db.session.add(novo_pedido)
        db.session.commit()



        for produtos in carrinho:
            produto = Produto.query.filter_by(id=produtos.id_produto).first()
            novo_produtopedido = ProdutoPedido(quantidade=produtos.quantidade, valor=produto.preco, id_produto = produtos.id, id_pedido=novo_pedido.id)
            db.session.add(novo_produtopedido)
            db.session.commit()
            db.session.delete(produtos)
            db.session.commit()
        pedido = Pedido.query.filter_by(id=novo_pedido.id).first()
        produto_pedido = ProdutoPedido.query.filter_by(id_pedido=pedido.id)
    return render_template("pedidos.html", usuario=current_user, produto_pedido=produto_pedido, total = total, valor=valor, cliente=cliente )


@carrinhoController.route("/pedidos", methods=['GET','POST'])
@login_required
def pedidos():
    cliente = Cliente.query.filter_by(id_usuario=current_user.id).first()
    pedidos = Pedido.query.filter_by(id_cliente=cliente.id)
    
    
    return render_template("listaPedidos.html", usuario=current_user, pedidos = pedidos)
