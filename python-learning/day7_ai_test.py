from ai_user import AIUser
from ai_manager import AIUserManager

user1=AIUser(
    "西瓜",
    "GPT_5",
    10000
)

manager=AIUserManager()

manager.add_user(user1)
 
manager.show_users()

print(manager.count_users())

manager.delete_user("西瓜")

print(manager.count_users())