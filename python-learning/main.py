user = {
    "name":"张三",
    "age":30
    }

import json

with open("users.json","w",encoding="utf-8") as file:
    json.dump(user,file,ensure_ascii=False)