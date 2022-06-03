from flask import Blueprint, render_template, request, redirect, url_for
from app.models.tables import Usuario
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
                return redirect(url_for('controllers.index', usuario=current_user))
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
        email = request.form.get('nome')
        password1 = request.form.get('password')
        password2 = request.form.get('confirmPassword')

        usuario = Usuario.query.filter_by(email=email).first()
        if usuario:
            return 'email já existente'
        elif len(email) < 4:
            return 'email curto'
        elif password1 != password2:
            return 'senhas diferentes'
        elif len(password1) < 4:
            return 'senha curta'
        else:
            novo_usuario = Usuario(email=email, admin=False, senha=password1)
            db.session.add(novo_usuario)
            db.session.commit()
            login_user(novo_usuario, remember=True)
            return redirect(url_for('controllers.index'))

    return render_template('cadastro.html', usuario=current_user)
