class AIUserManager:
    def __init__(self):
        self.users=[]

    def add_user(self,user):
        self.users.append(user)

    def show_users(self):
        for user in self.users:
            print(user.__dict__)

    def count_users(self):
        return len(self.users)

    def delete_user(self,name):
        for user in self.users:
            if user.name == name:
                self.users.remove(user)
                return True
        
        return False
