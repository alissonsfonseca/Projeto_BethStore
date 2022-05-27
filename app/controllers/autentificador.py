from flask import Blueprint, render_template, request, redirect, url_for
from app.models.tables import Usuario
from flask_login import login_user, login_required, logout_user, current_user
from app import db
from werkzeug.security import generate_password_hash, check_password_hash


autentificador = Blueprint('autentificador', __name__)

@autentificador.route('login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        nome_usuario = request.form.get('nome_usuario')
        senha = request.form.get('senha')

        usuario = Usuario.query.filter_by(nome_usuario=nome_usuario).first()

        if usuario:
            if check_password_hash(usuario.senha, senha):
                login_user(usuario, remember=True)
                return redirect(url_for('controllers'))
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
