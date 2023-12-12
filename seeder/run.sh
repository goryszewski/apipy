sleep 20
mysql --host=mysql --user=root --password="$(< /run/secrets/db_root_password)" < /mnt/init.sql
