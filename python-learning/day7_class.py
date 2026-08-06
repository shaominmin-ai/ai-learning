class User:

    def __init__(self,name,goal,age):
        self.name=name
        self.goal=goal
        self.age=age

    def introduce(self):
        print(f"我是{self.name},我的目标是{self.goal}")

    def change_goal(self,new_goal):
        self.goal=new_goal

    def say_hi(self):
        print(f"{self.name}你好")
    
    def show_info(self):
        print(f"姓名:{self.name},目标:{self.goal},年龄:{self.age}")


user1 = User("小明","Python开发",30)
user2 = User("西瓜","AI",31)

user1.introduce()
user2.introduce()

user1.change_goal("AI应用开发")
user2.change_goal("AI Agent开发")

user1.introduce()
user2.introduce()

user1.say_hi()
user2.say_hi()

user1.show_info()
user2.show_info()
