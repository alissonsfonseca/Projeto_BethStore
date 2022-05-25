from app import db

class Usuario(db.Model):
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