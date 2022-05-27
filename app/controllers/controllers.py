from flask import Blueprint , render_template, redirect, url_for, request
from flask_login import login_required, current_user
from app import db 

controllers = Blueprint('controllers', __name__)

@controllers.route('/')
def index():
    return render_template('index.html')