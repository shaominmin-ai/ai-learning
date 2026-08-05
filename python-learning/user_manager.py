import json

def get_users():

    with open("users.json","r") as file:
        users=json.load(file)

    return users

def count_users():
    users=get_users()
    return len(users)