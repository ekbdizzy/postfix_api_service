# API-server to manage postfix mailboxes.

The idea of this implementation is to automize managing of bulk creating, updating, deleting mailboxes.
Also, I'm going to add functional to read letters by account name or by pattern and automatic send letters.

# SETUP

1. Install python>3.11.
2. Create virtualenv and activate it:
```shell
cd project_dir
python3.11 -m venv venv
source venv/bin/activate
```
3. Install packages:
```pip install -r requirements```
If you have a troubles here, try to run:
```shell
sudo apt install python3-full
```
4. Create `.env` file with `DB_URL`, which depends on your database.

`DB_URL=CONNECTOR://YOUR_USER:PASSWORD@HOST:PORT/postfix`

Change connector, user, password, host, port with your credentials.

Use connector for:
- MySQL: `mysql+mysqlconnector`
- MariaDB: `mariadb+mariadbconnector`or `mariadb+mariadbconnector`<br>
You can also use MySQL connector, if you want. Learn more [here.](https://docs.sqlalchemy.org/en/20/dialects/mysql.html)
- PostgreSQL: `postgresql`

Example for `.env` file:
```shell
DB_URL=mysql+mysqlconnector://user:my_password@localhost:3306/postfix
```
