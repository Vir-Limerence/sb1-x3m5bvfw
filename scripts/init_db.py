from pymongo import MongoClient
import bcrypt
import os

def init_root_user():
    # MongoDB connection
    mongo_uri = os.getenv('MONGO_URI', 'mongodb://localhost:27017/')
    db_name = os.getenv('MONGO_DB', 'security_analysis')
    
    client = MongoClient(mongo_uri)
    db = client[db_name]
    users = db['users']
    
    # Check if root user already exists
    if users.find_one({'username': 'root'}):
        print("Root user already exists")
        return
    
    # Create root user
    password = 'root'
    salt = bcrypt.gensalt()
    hashed = bcrypt.hashpw(password.encode('utf-8'), salt)
    
    root_user = {
        'username': 'root',
        'password': hashed,
        'is_admin': True,
        'created_at': datetime.utcnow()
    }
    
    users.insert_one(root_user)
    print("Root user created successfully")

if __name__ == '__main__':
    init_root_user()