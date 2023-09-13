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
4. Create `.env` file with following settings:
```
DB_USER=root
DB_PASSWORD=password
DB_NAME=postfix
DB_HOST=localhost
DB_PORT=3306
```