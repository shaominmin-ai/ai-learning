import user_manager
import logging

logging.basicConfig(
    level=logging.INFO,
    filename="app.log"
)

while True:

    print("=================")
    print("AI用户管理系统")
    print("=================")

    print("1.查看用户")
    print("2.添加用户")
    print("3.删除用户")
    print("4.更改用户")
    print("5.退出")
    print("6.查看用数量")

    choice = input("请选择:")

    if choice == "1":
        users = user_manager.get_users()
        print(users)
    
    elif choice == "2":
        name=input("请输入名字:")
        goal=input("请输入目标:")

        new_user={
            "name":name,
            "goal":goal
        }
        user_manager.add_user(new_user)
        print("添加成功")
        logging.info(
            f"添加用户:{name}"
        )

    elif choice == "3":
        name=input("请输入要删除的用户:")
        result=user_manager.delete_user(name)
        if result:
            print("删除成功")
        else:
            print("用户不存在")    

    elif choice == "4":
        name=input("需要修改的用户名：")
        new_goal=input("请输入新目标:")
        result=user_manager.update_user(name,new_goal)
        if result:
            print("更改成功")
        else:
            print("用户不存在")


    elif choice == "5":
        print("退出系统")
        break
    
    elif choice =="6":
        count = user_manager.count_users()
        print(f"当前用户数量:{count}")
