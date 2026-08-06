import json

def get_users():
    try:

        with open("users.json","r") as file:
            users=json.load(file)

        return users

    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_users(users):
    with open("users.json","w") as file:
        json.dump(users,file)


def count_users():
    users=get_users()
    return len(users)

def add_user(user):
    users=get_users()
    users.append(user)
    save_users(users)

def delete_user(name):
    users=get_users()
    for user in users:
        if user["name"] == name:
            users.remove(user)
            save_users(users)
            return True

    return False

def update_user(name,new_goal):
    users=get_users()
    for user in users:
        if user["name"] == name:
            user["goal"]=new_goal
            save_users(users)
            return True
    
    return False

