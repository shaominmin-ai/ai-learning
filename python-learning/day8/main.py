from user_manager import UserManager

manager = UserManager()

new_user = manager.create_user("李四")

print("创建：")
print(new_user)

print("删除前：")
print(manager.get_users())

result = manager.delete_user(2)

print("删除结果：")
print(result)

print("删除后：")
print(manager.get_users())