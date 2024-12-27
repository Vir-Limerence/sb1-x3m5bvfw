from pymongo import MongoClient
from flask import current_app

def get_db():
    client = MongoClient(current_app.config['MONGO_URI'])
    return client[current_app.config['MONGO_DB']]

def get_collection(collection_name):
    db = get_db()
    return db[collection_name]