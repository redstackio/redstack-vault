---
id: eecdae9a-05d3-4fd2-b00b-e474a40b5954
name: Retrieve MySQL User ID
type: command
executor: bash
data: '$ mysql -u root -p mysql

  Enter password: [...]

  mysql> SELECT sys_eval(''id'');

  +--------------------------------------------------+

  | sys_eval(''id'') |

  +--------------------------------------------------+

  | uid=118(mysql) gid=128(mysql) groups=128(mysql) |

  +--------------------------------------------------+'
output: null
created_at: '2023-04-06T03:56:34.964267+00:00'
updated_at: '2023-04-10T20:22:59.153732+00:00'
---

# Retrieve MySQL User ID

```bash
$ mysql -u root -p mysql
Enter password: [...]
mysql> SELECT sys_eval('id');
+--------------------------------------------------+
| sys_eval('id') |
+--------------------------------------------------+
| uid=118(mysql) gid=128(mysql) groups=128(mysql) |
+--------------------------------------------------+
```


