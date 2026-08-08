# AI Learning Journey

## 我的目标

通过 180 天学习，成为 AI 应用开发者。

## 当前阶段

**Day 1** — 学习 Cursor 和 AI 开发流程。

## 后续计划

- 学习 Python
- Web 开发
- AI API
- RAG
- Agent

Day6 completed:

- Exception handling
- Logging system
- Git version update

# Day7 Python 面向对象（OOP）

## 今日目标

学习 Python 面向对象基础：

- class（类）
- object（对象）
- **init** 初始化方法
- self
- 方法（method）
- 对象属性
- 模块导入
- 对象管理器
- CRUD思想

---

# 1. 什么是 class？

class 是对象的模板。

例如：

```

```

```
class AIUser:
    pass
```

这里创建了一个 AIUser 模板。

但是它还不是一个真实用户。

类似：

> class = 用户信息表格模板

---

# 2. 创建对象 object

通过类创建具体对象：

```

```

```
user1 = AIUser()
```

此时：

```

```

```
AIUser
  |
  ↓
user1对象
```

user1 是 AIUser 类创建出来的实例。

---



# 3. **init** 初始化方法

代码：

```

```

```
class AIUser:

    def __init__(self,name,model,tokens):
        self.name=name
        self.model=model
        self.tokens=tokens
```

作用：

当创建对象时，自动执行。

例如：

```

```

```
user1=AIUser(
    "西瓜",
    "GPT_5",
    10000
)
```

自动执行：

```

```

```
self.name="西瓜"
self.model="GPT_5"
self.tokens=10000
```

---



# 4. self是什么？

这是今天最重要的概念。

self：

代表当前对象自己。

例如：

```

```

```
user1=AIUser(
    "西瓜",
    "GPT_5",
    10000
)
```

那么：

```

```

```
self.name
```

实际上就是：

```

```

```
user1.name
```

例如：

```

```

```
print(user1.name)
```

输出：

```

```

```
西瓜
```

---



## 为什么每个方法都有self？

因为方法需要知道：

> 是哪个对象调用它

例如：

```

```

```
user1.show_info()
```

Python实际理解：

```

```

```
AIUser.show_info(user1)
```

所以必须有：

```

```

```
def show_info(self):
```

---



# 5. 对象属性

对象内部保存的数据：

例如：

```

```

```
user1.__dict__
```

输出：

```

```

```
{
'name':'西瓜',
'model':'GPT_5',
'tokens':10000
}
```

**dict**：

作用：

把对象内部属性转换成字典形式。

---



# 6. 方法 method

类里面定义的函数叫方法。

例如：

```

```

```
def say_hi(self):
    print(f"{self.name}你好")
```

调用：

```

```

```
user1.say_hi()
```

输出：

```

```

```
西瓜你好
```

---



# 7. 模块导入

把代码拆成多个文件。

例如：

ai_[user.py](http://user.py)

保存：

```

```

```
class AIUser:
```

另一个文件：

```

```

```
from ai_user import AIUser
```

然后使用：

```

```

```
user1=AIUser(...)
```

好处：

大型项目不会所有代码写在一个文件。

---



# 8. Manager管理器思想

今天创建：

```

```

```
class AIUserManager:
```

作用：

管理多个 AIUser。

结构：

```

```

```
AIUser
 |
 | 保存用户信息


AIUserManager
 |
 | 管理多个AIUser
```

---



# 9. 用户列表

初始化：

```

```

```
def __init__(self):
    self.users=[]
```

创建：

```

```

```
manager=AIUserManager()
```

内部：

```

```

```
users=[]
```

---

添加用户：

```

```

```
manager.add_user(user1)
```

执行：

```

```

```
self.users.append(user)
```

结果：

```

```

```
users=[
    西瓜对象
]
```

---



# 10. 查看用户

代码：

```

```

```
def show_users(self):

    for user in self.users:
        print(user.__dict__)
```

逻辑：

遍历所有用户：

```

```

```
users列表

 ↓

一个一个取出来

 ↓

打印用户信息
```

---



# 11. 用户数量统计

代码：

```

```

```
def count_users(self):

    return len(self.users)
```

例如：

```

```

```
[
 西瓜
]
```

长度：

```

```

```
1
```

---



# 12. 删除用户

代码：

```

```

```
def delete_user(self,name):

    for user in self.users:

        if user.name == name:

            self.users.remove(user)

            return True

    return False
```

流程：

```

```

```
遍历用户

↓

找到名字

↓

删除对象

↓

返回True
```

如果不存在：

返回：

```

```

```
False
```

---



# 13. CRUD概念（非常重要）

真实软件几乎都有：


| 功能  | 英文     | 代码          |
| --- | ------ | ----------- |
| 增加  | Create | add_user    |
| 查询  | Read   | show_users  |
| 修改  | Update | change_goal |
| 删除  | Delete | delete_user |


今天你的 AIUserManager 已经完成基础 CRUD。





# Day8 文件持久化与CRUD系统

日期：

2026-08-08

---

# 一、今日学习目标

今天开始从“写代码”进入“开发应用”。

之前：

程序运行：

```

```

```
Python变量
    ↓
内存
    ↓
程序关闭
    ↓
数据消失
```

今天学习：

让程序拥有“记忆”。

实现：

```

```

```
Python程序

    ↓

文件存储

    ↓

永久保存数据
```

---

# 二、核心概念：数据持久化

## 什么是持久化？

持久化：

> 将程序运行中的数据保存到外部存储，使程序关闭后数据仍然存在。

例如：

之前：

```

```

```
users = []
```

数据存储：

```

```

```
RAM内存
```

程序关闭：

```

```

```
数据消失
```

升级：

```

```

```
users列表

↓

users.json

↓

硬盘保存
```

重新启动：

```

```

```
users.json

↓

读取

↓

恢复数据
```

---

# 三、文件操作基础

## 1. open()

Python打开文件：

```

```

```
open(
    文件名,
    模式,
    编码
)
```

例如：

```

```

```
with open(
    "users.json",
    "w",
    encoding="utf-8"
) as file:
```

---

## 2. 文件模式


| 模式  | 含义        |
| --- | --------- |
| r   | read，读取   |
| w   | write，写入  |
| a   | append，追加 |


---

# 四、UTF-8编码

## 为什么需要编码？

电脑底层只能识别：

```

```

```
01010101
```

文字需要转换成数字。

编码就是：

> 字符和数字之间的转换规则。

---

## UTF-8

目前最常用的全球字符编码。

例如：

```

```

```
张三
```

通过UTF-8转换：

```

```

```
文字

↓

二进制数据

↓

保存文件
```

代码：

```

```

```
encoding="utf-8"
```

表示：

使用UTF-8保存和读取文件。

---

# 五、JSON数据转换

Python对象：

```

```

```
user = {
    "name":"张三",
    "age":30
}
```

需要保存：

转换为JSON。

---

## json.dump()

作用：

Python → JSON

代码：

```

```

```
json.dump(
    user,
    file,
    ensure_ascii=False,
    indent=4
)
```

---

## json.load()

作用：

JSON → Python

代码：

```

```

```
users=json.load(file)
```

---

# 六、ensure_ascii=False

作用：

控制中文显示。

默认：

```

```

```
ensure_ascii=True
```

可能：

```

```

```
{
"name":"\u5f20\u4e09"
}
```

关闭：

```

```

```
ensure_ascii=False
```

显示：

```

```

```
{
"name":"张三"
}
```

开发项目时通常使用：

```

```

```
ensure_ascii=False
```

---

# 七、indent=4

作用：

格式化JSON。

不使用：

```

```

```
{"id":1,"name":"张三"}
```

使用：

```

```

```
indent=4
```

结果：

```

```

```
{
    "id":1,
    "name":"张三"
}
```

方便人阅读。

---

# 八、项目实战：UserManager升级

项目结构：

```

```

```
day8

├── main.py

├── user_manager.py

├── users.json

└── app.log

```

---

# 九、UserManager设计

## 类结构

```

```

```
UserManager

│

├── __init__()

│       ↓

│   设置数据文件


├── load_users()

│       ↓

│   读取JSON


├── save_users()

│       ↓

│   保存JSON


├── create_user()

│       ↓

│   创建用户


├── get_users()

│       ↓

│   查询用户


└── delete_user()

        ↓

    删除用户

```

---

# 十、CRUD概念

CRUD代表：

## C - Create

创建

代码：

```

```

```
create_user()
```

流程：

```

```

```
输入用户信息

↓

读取已有数据

↓

创建对象

↓

加入列表

↓

保存文件
```

---

## R - Read

读取

代码：

```

```

```
get_users()
```

流程：

```

```

```
users.json

↓

json.load()

↓

Python列表

↓

返回
```

---

## U - Update

更新

今天未实现。

未来数据库中学习。

---

## D - Delete

删除

代码：

```

```

```
delete_user()
```

流程：

```

```

```
读取用户

↓

for循环查找id

↓

remove删除

↓

保存数据

↓

返回结果
```

---

# 十一、logging日志系统

为什么需要日志？

真实产品：

用户：

“系统失败了”

开发者需要知道：

-  什么时间 
-  什么用户 
-  什么错误 

---

配置：

```

```

```
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)
```

---

日志等级：

```

```

```
DEBUG

↓

INFO

↓

WARNING

↓

ERROR

↓

CRITICAL
```

---

记录：

创建成功：

```

```

```
logging.info(
    f"创建用户成功:{user}"
)
```

删除成功：

```

```

```
logging.info(
    f"删除用户成功:{user}"
)
```

---

# 十二、今日遇到的问题

## 1. 字符串缺少引号

错误：

```

```

```
SyntaxError:
EOL while scanning string literal
```

原因：

字符串没有结束。

例如：

错误：

```

```

```
"name":"张三
```

正确：

```

```

```
"name":"张三"
```

---

## 2. Python缩进错误

错误：

```

```

```
IndentationError
```

原因：

Python使用缩进表示代码层级。

例如：

错误：

```

```

```
if condition:

print()
```

正确：

```

```

```
if condition:

    print()
```

---

## 3. 点号和逗号区别

错误：

```

```

```
manager,get_users()
```

正确：

```

```

```
manager.get_users()
```

区别：

`.`

调用对象方法。

`,`

表示两个独立对象。

---

## 4. NameError

例如：

```

```

```
name 'users' is not defined
```

原因：

变量不存在。

解决：

检查：

-  是否创建变量 
-  是否作用域正确 

---

# 十三、Git提交

提交信息：

```

```

```
Day8 complete: JSON persistence CRUD UserManager
```

完成：

```

```

```
git add .

git commit

git push
```

---

# 十四、今日最大收获

今天第一次完成：

## 一个有记忆的小程序

从：

```

```

```
代码

↓

运行

↓

结束
```

升级：

```

```

```
代码

↓

读取数据

↓

处理逻辑

↓

保存数据

↓

下次继续使用
```

---

# 十五、与AI产品的关系

未来AI应用：

例如：

建筑AI助手：

用户：

```

```

```
项目经理A
```

上传：

```

```

```
合同.pdf

施工图.dwg

签证资料.xlsx
```

系统需要保存：

```

```

```
用户信息

项目资料

文件记录

分析结果

权限
```

本质都是：

今天学习的：

```

```

```
数据持久化

↓

数据库

↓

AI应用数据层
```

---

# Day8总结

完成：

✅ 文件读写  
 ✅ JSON持久化  
 ✅ UTF-8编码  
 ✅ json.dump  
 ✅ json.load  
 ✅ UserManager升级  
 ✅ CRUD系统  
 ✅ logging日志  
 ✅ Git提交

今日项目：

```

```

```
JSON版用户管理系统
```

