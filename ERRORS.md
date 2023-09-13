if you have an error:
`_mysql_connector.MySQLInterfaceError: Access denied for user 'root'@'localhost'`,
go to mysql:
```shell
mysql -u root -p
```
and try to add access:
```sql
GRANT ALL PRIVILEGES ON postfix.* TO 'root'@'localhost';
FLUSH PRIVILEGES;
ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'password';
```
