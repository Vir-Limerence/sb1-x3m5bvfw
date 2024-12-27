from database.mongo_client import get_collection
import bcrypt

class User:
    @staticmethod
    def create_user(username: str, password: str) -> dict:
        users = get_collection('users')
        
        # Check if user already exists
        if users.find_one({'username': username}):
            return {'success': False, 'message': 'Username already exists'}
            
        # Hash password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
        
        user_doc = {
            'username': username,
            'password': hashed
        }
        
        users.insert_one(user_doc)
        return {'success': True, 'message': 'User created successfully'}
    
    @staticmethod
    def verify_user(username: str, password: str) -> bool:
        users = get_collection('users')
        user = users.find_one({'username': username})
        
        if not user:
            return False
            
        return bcrypt.checkpw(password.encode('utf-8'), user['password'])