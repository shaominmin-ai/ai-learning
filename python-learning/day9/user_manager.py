from database import get_connection

class UserManager:

    def __init__(self):
        self.conn = get_connection()

    def create_user(self,name):
        cursor = self.conn.cursor()

        cursor.execute(
            """
            INSERT INTO users(name)
            VALUES(?)
            """,
            (name,)
        )

        self.conn.commit()

        return True

    def get_users(self):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            SELECT * FROM users
            """
        )

        rows = cursor.fetchall()

        users = []
        for row in rows:
            user = {
                "id":row[0],
                "name":row[1]
            }
            users.append(user)

        return users

    def delete_user(self,user_id):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            DELETE FROM users
            WHERE id=?
            """,
            (user_id,)
        )

        self.conn.commit()

        return True

    def update_user(self,user_id,new_name):

        cursor = self.conn.cursor()

        cursor.execute(
            """
            UPDATE users
            SET name=?
            WHERE id=?
            """,
            (new_name,user_id)
        )
        self.conn.commit()
        return True
