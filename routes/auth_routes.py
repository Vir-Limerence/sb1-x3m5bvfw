from flask import Blueprint, request, jsonify
from services.auth_service import AuthService
from utils.request_utils import validate_json

auth_bp = Blueprint('auth', __name__)
auth_service = AuthService()

@auth_bp.route('/login', methods=['POST'])
@validate_json(['username', 'password'])
def login():
    data = request.get_json()
    result = auth_service.login(data['username'], data['password'])
    return jsonify(result)

@auth_bp.route('/register', methods=['POST'])
@validate_json(['username', 'password'])
def register():
    data = request.get_json()
    result = auth_service.register(data['username'], data['password'])
    return jsonify(result)