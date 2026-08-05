import user_manager

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

    elif choice == "5":
        print("退出系统")
        break
    
    elif choice =="6":
        count = user_manager.count_users()
        print(f"当前用户数量:{count}")
        