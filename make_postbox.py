import bcrypt
import mysql.connector

config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "postfix",
    "autocommit": True,
    "auth_plugin": "mysql_native_password",
}

connection = mysql.connector.connect(**config)
cursor = connection.cursor()

cursor.execute("SELECT * FROM mailbox")
rows = cursor.fetchall()

for row in rows:
    print(row)

def encrypt_password(password: str) -> str:
    return str(bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()))