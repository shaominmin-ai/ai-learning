from user_manager import UserManager

manager = UserManager()

print("创建用户")
manager.create_user("赵六")

print("当前用户:")
print(manager.get_users())

print("删除用户id=1")
manager.delete_user(1)

print("删除后:")
print(manager.get_users())

print("修改用户")
manager.update_user(
    2,
    "李明"
)
print(manager.get_users())