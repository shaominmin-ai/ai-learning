from uesr import User
from user_manager import AIUser

user1=AIUser(
    "西瓜",
    "GPT_5",
    "10000"
)

manager=AIUserManager()

manager.add_uesr(user1)
 
manager.show_users()