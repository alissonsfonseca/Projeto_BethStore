from app import db
from flask_login import UserMixin

class Usuario(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    admin = db.Column(db.Boolean, default = False)
    nome_usuario = db.Column(db.String)
    senha = db.Column(db.String)

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

    id_categoria = db.Column(db.Integer, db.ForeignKey("categoria.id"))
    categoria = db.relationship("Categoria", foreign_keys = id_categoria)

class Categoria(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    descricao = db.Column(db.String)
    setor = db.Column(db.String)

class Carrinho(db.Model):
    quantidade = db.Column(db.Integer)
    valor_frete = db.Column(db.Float)
    previsao_entrega = db.Column(db.Integer)
    
    id_cliente = db.Column(db.Integer, db.ForeignKey("cliente.id"), primary_key = True)
    cliente = db.relationship("Cliente", foreign_keys = id_cliente)
    id_produto = db.Column(db.Integer, db.ForeignKey("produto.id"), primary_key = True)
    produto = db.relationship("Produto", foreign_keys = id_produto)



