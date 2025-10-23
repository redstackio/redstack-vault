---
id: 0b432b09-c424-4a72-a0bb-34e97a643b80
name: Database Dump
type: command
executor: bash
data: sqlmap.py -d "mysql://user:pass@ip/database" --dump-all
output: null
created_at: '2023-04-06T03:56:36.526980+00:00'
updated_at: '2023-04-10T20:24:27.086249+00:00'
---

# Database Dump

```bash
sqlmap.py -d "mysql://user:pass@ip/database" --dump-all
```


