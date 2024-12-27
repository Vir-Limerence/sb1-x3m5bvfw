def get_all_users():
    # In a real application, this would interact with a database
    return [
        {'id': 1, 'name': 'User 1'},
        {'id': 2, 'name': 'User 2'}
    ]

def create_user(data):
    # In a real application, this would save to a database
    return {'id': 3, **data}