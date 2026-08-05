import json

def get_users():

    with open("users.json","r") as file:
        users=json.load(file)

    return users
