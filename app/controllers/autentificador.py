from flask import Blueprint, render_template, request, redirect, url_for
from app.models.tables import Usuario, Cliente
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


autentificador = Blueprint('autentificador', __name__)

@autentificador.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        senha = request.form.get('password')

        usuario = Usuario.query.filter_by(email=email).first()

        if usuario:
            if check_password_hash(usuario.senha, senha):
                login_user(usuario, remember=True)
                return redirect(url_for('controllers.index'))
            else:
                return 'senha incorreta'
        else:
            return 'usuario inexistente'
        
    return render_template("login.html", usuario=current_user)

@autentificador.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('autentificador.login'))

@autentificador.route('/cadastro', methods = ['GET','POST'])
def cadastro():
    if request.method == 'POST':
        email = request.form.get('email')
        password1 = request.form.get('password')
        password2 = request.form.get('confirmPassword')
        nome = request.form.get('nome')
        cpf = request.form.get('cpf')
        endereco = request.form.get('endereco')
        telefone = request.form.get('telefone')
        cep = request.form.get('cep')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            return 'email já existente'
        elif len(email) < 4:
            return 'email curto'
        elif password1 != password2:
            return 'senhas diferentes'
        elif len(password1) < 4:
            return 'senha curta'
        elif len(nome) < 4:
            return 'nome curto'
        elif len(cpf) < 8:
            return 'cpf curto'
        elif len(endereco) < 4:
            return 'endereço curto'
        elif len(telefone) < 4:
            return 'telefone curto'
        elif len(cep) < 4:
            return 'cep curto'
        else:
            novo_usuario = Usuario(email=email, admin=False, senha=generate_password_hash(password1, method='sha256'))
            db.session.add(novo_usuario)
            db.session.commit()
            login_user(novo_usuario, remember=True)
            novo_cliente = Cliente(nome=nome, cpf=cpf, endereco=endereco, telefone=telefone, cep=cep, id_usuario=current_user.id)
            db.session.add(novo_cliente)
            db.session.commit()
            return redirect(url_for('controllers.index'))

    return render_template('cadastro.html', usuario=current_user)
