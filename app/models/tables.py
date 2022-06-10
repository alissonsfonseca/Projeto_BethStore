from app import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from re import U

class Imagem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    img = db.Column(db.String)
    name = db.Column(db.String)
    mimetype = db.Column(db.String)

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    admin = db.Column(db.Boolean, default = False)
    senha = db.Column(db.String)
    email = db.Column(db.String)

class Cliente(db.Model):
    id  = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String)
    cpf = db.Column(db.String)
    endereco = db.Column(db.String)
    telefone = db.Column(db.String)
    cep = db.Column(db.String)

    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    usuario = db.relationship("Usuario", foreign_keys = id_usuario)

class Produto(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    marca = db.Column(db.String)
    modelo = db.Column(db.String)
    preco = db.Column(db.Float)
    tamanho = db.Column(db.String)
    quantidade = db.Column(db.Integer)
    inf_tecnica = db.Column(db.String)
    descricao = db.Column(db.String)
    
    id_imagem = db.Column(db.Integer, db.ForeignKey("imagem.id"))
    imagem = db.relationship("Imagem", foreign_keys = id_imagem)

    id_categoria = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    categoria = db.relationship("Categoria", foreign_keys = id_categoria)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    descricao = db.Column(db.String)
    nome = db.Column(db.String)
    
    id_setor = db.Column(db.Integer, db.ForeignKey("setor.id"))
    setor = db.relationship("Setor", foreign_keys = id_setor)
    
class Setor(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nome = db.Column(db.String)

class Carrinho(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    quantidade = db.Column(db.Integer)
    valor_frete = db.Column(db.Float)
    previsao_entrega = db.Column(db.Integer)
    
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    cliente = db.relationship("Cliente", foreign_keys = id_cliente)
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"))
    produto = db.relationship("Produto", foreign_keys = id_produto)

class Pedido(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    valor_frete = db.Column(db.Float)
    previsao_entrega = db.Column(db.Integer)
    forma_pagamento = db.Column(db.String)
    pagamento = db.Column(db.String)
    total = db.Column(db.Float)

    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"))
    cliente = db.relationship("Cliente", foreign_keys = id_cliente)
    id_aprovacao = db.Column(db.Integer, db.ForeignKey("aprovacao.id"))
    aprovacao = db.relationship("Aprovacao", foreign_keys = id_aprovacao)
    
class Aprovacao(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    mensagem = db.Column(db.String)

    id_usuario = db.Column(db.Integer, db.ForeignKey("usuario.id"))
    usuario = db.relationship("Usuario", foreign_keys = id_usuario)

class ProdutoPedido(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    quantidade = db.Column(db.Integer)
    valor = db.Column(db.Float)
    
    id_pedido = db.Column(db.Integer, db.ForeignKey("pedido.id"), primary_key = True)
    pedido = db.relationship("Pedido", foreign_keys = id_pedido)
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key = True)
    produto = db.relationship("Produto", foreign_keys = id_produto)



