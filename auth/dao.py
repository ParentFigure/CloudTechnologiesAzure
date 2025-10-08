from .models import *

from flask import current_app


class UserDAO:
    @staticmethod
    def get_all_users():
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM User")
            users = [User(row[0],row[1],row[2],row[3],row[4],row[5]) for row in cursor.fetchall()]
        except Exception as e:
            print(f"Error fetching users: {e}")
            users = []
        finally:
            cursor.close()
        return users

    @staticmethod
    def get_user_by_id(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("SELECT * FROM User WHERE user_id = %s", (user_id,))
            row = cursor.fetchone()
            row=User(row[0],row[1],row[2],row[3],row[4],row[5])
        except Exception as e:
            print(f"Error fetching user: {e}")
            row = None
        finally:
            cursor.close()
        return row

    @staticmethod
    def add_user(username, email, password, account_status, registration_date):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                "INSERT INTO User (username, email, password, account_status, registration_date) VALUES (%s, %s, %s, %s, %s)",
                (username, email, password, account_status, registration_date)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error adding user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def update_user(user_id, username, email, password, account_status, registration_date):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute(
                """UPDATE User 
                   SET username = %s, email = %s, password = %s, account_status = %s, registration_date = %s 
                   WHERE user_id = %s""",
                (username, email, password, account_status, registration_date, user_id)
            )
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error updating user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

    @staticmethod
    def delete_user(user_id):
        try:
            cursor = current_app.mysql.connection.cursor()
            cursor.execute("DELETE FROM User WHERE user_id = %s", (user_id,))
            current_app.mysql.connection.commit()
        except Exception as e:
            print(f"Error deleting user: {e}")
            current_app.mysql.connection.rollback()
        finally:
            cursor.close()

# Інші таблиці мають схожу структуру побудови, тому для прикладу взяла лише одну з таблиць
