from flask import Blueprint, jsonify, request
from services.user_service import get_all_users, create_user

user_bp = Blueprint('user', __name__)

@user_bp.route('/', methods=['GET'])
def get_users():
    users = get_all_users()
    return jsonify(users)

@user_bp.route('/', methods=['POST'])
def add_user():
    data = request.get_json()
    user = create_user(data)
    return jsonify(user), 201