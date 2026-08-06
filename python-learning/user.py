class User:

    def __init__(self,name,goal,age):
        self.name=name
        self.goal=goal
        self.age=age

    def introduce(self):
        print(f"我是{self.name},目标是{self.goal},年龄{self.age}")
        