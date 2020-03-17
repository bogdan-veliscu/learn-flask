from user import User

users = [
    User(1, 'bogdan', 's3cret'),
    User(2, 'georgi', "pass")
]

user_mapping = {u.username: u for u in users}
userid_mapping = {u.id: u for u in users}


def authenticate(username, password):
    user = user_mapping.get(username, None)
    if user and user.password == password:
        return user


def identity(payload):
    user_id = payload['identity']
    return userid_mapping.get(user_id, None)
