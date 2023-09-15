# Errors

`_mysql_connector.MySQLInterfaceError: Access denied for user 'root'@'localhost'`, <br>
1. Go to mysql:
```shell
mysql -u root -p
```
2. Try to add access:
```sql
GRANT ALL PRIVILEGES ON postfix.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```

---
`MariaDB Connector/C is not installed`:
```shell
sudo apt install libmariadb3 libmariadb-dev
```

---
`MariaDB Connector/Python requires MariaDB Connector/C >= 3.3.1, found version 3.*.*.` <br>
Here is [solution from StackOverFlow.](https://stackoverflow.com/questions/63628125/error-pip-install-mariadb-on-ubuntu-server)
---
