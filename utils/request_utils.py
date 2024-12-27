from functools import wraps
from flask import request, jsonify
from typing import List

def validate_json(required_fields: List[str]):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if not request.is_json:
                return jsonify({'success': False, 'message': '请求必须是JSON格式'}), 400
            
            data = request.get_json()
            missing_fields = [field for field in required_fields if field not in data]
            
            if missing_fields:
                return jsonify({
                    'success': False,
                    'message': f'缺少必需的字段: {", ".join(missing_fields)}'
                }), 400
                
            return f(*args, **kwargs)
        return decorated_function
    return decorator

def validate_files(required_files: List[str]):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            missing_files = [file for file in required_files if file not in request.files]
            
            if missing_files:
                return jsonify({
                    'success': False,
                    'message': f'缺少必需的文件: {", ".join(missing_files)}'
                }), 400
                
            return f(*args, **kwargs)
        return decorated_function
    return decorator