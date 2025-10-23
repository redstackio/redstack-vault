---
id: 33a11b5f-a789-4a5b-b4d6-1e78da976c22
name: SQL Injection scan using sqlmap
type: command
executor: bash
data: sqlmap -u "http://www.target.com" --proxy="http://127.0.0.1:8080"
output: null
created_at: '2023-04-06T03:56:36.424482+00:00'
updated_at: '2023-04-10T20:24:18.090082+00:00'
---

# SQL Injection scan using sqlmap

```bash
sqlmap -u "http://www.target.com" --proxy="http://127.0.0.1:8080"
```


