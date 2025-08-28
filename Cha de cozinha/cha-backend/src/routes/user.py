# src/routes/user.py
from flask import Blueprint

# Blueprint do usuário
user_bp = Blueprint('user', __name__)

@user_bp.route('/users')
def users():
    return "Rota de usuários funcionando!"
