import json

from user import User

user1 = User(
    "小明",
    "Python开发",
    30
)

user_dict =user1.__dict__

with open(
    "user_test.json",
    "w"
) as file:

    json.dump(
        user_dict,
        file
    )