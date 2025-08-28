from flask import Blueprint
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def users():
    return "Rota de usuários funcionando!"