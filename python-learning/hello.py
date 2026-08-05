import json

with open("users.json","r") as file:
    users=json.load(file)

search_name=input("请输入要删除的用户名:")

found=False


for user in users:
    if user["name"]==search_name:
        users.remove(user)
        found=True
        break

if found:
    with open("users.json","w") as file:
        json.dump(users,file)

    print("删除成功")
else:
    print("没有找到用户")
