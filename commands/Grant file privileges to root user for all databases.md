---
id: 27bb1736-8814-4ca8-93df-d5ae7beed0c2
name: Grant file privileges to root user for all databases
type: command
executor: bash
data: GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
output: null
created_at: '2023-04-06T03:56:34.767876+00:00'
updated_at: '2023-04-10T20:22:51.267705+00:00'
---

# Grant file privileges to root user for all databases

```bash
GRANT FILE ON *.* TO 'root'@'localhost'; FLUSH PRIVILEGES;
```


