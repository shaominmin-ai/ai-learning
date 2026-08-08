import json
import logging
logging.basicConfig(
    filename="app.log",
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

class UserManager:

    def __init__(self):
        self.file = "users.json"


    def load_users(self):

        try:

            with open(
                self.file,
                "r",
                encoding="utf-8"
            ) as file:

                return json.load(file)

        except:

            return []

    def save_users(self,users):

        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                users,
                file,
                ensure_ascii=False,
                indent=4
            )
    
    def create_user(self,name):
        users = self.load_users()

        user = {
            "id":len(users) + 1,
            "name":name
        }

        users.append(user)

        self.save_users(users)
        
        logging.info(
            f"创建用户成功:{user}"
        )

        return user

    def get_users(self):
        return self.load_users()

    def delete_user(self,user_id):
        users = self.load_users()

        for user in users:
            if user["id"] == user_id:
                users.remove(user)
                self.save_users(users)
                logging.info(
                    f"删除用户成功:{user}"
                )
                return True

        logging.warning(
            f"删除失败，用户不存在 id={user_id}"
            )
        return False