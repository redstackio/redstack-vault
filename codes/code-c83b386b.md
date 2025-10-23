---
id: c83b386b-3e86-43c8-9c72-bf2d9c6f0eb8
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:21.083249+00:00'
updated_at: '2023-04-10T20:36:46.098325+00:00'
---

# Code Snippet c83b386b

**Language**: SQL

```sql
SELECT SYSTEM_USER
SELECT IS_SRVROLEMEMBER('sysadmin')
EXECUTE AS LOGIN = 'stduser'
SELECT SYSTEM_USER
EXECUTE AS LOGIN = 'sa'
SELECT IS_SRVROLEMEMBER('sysadmin')
SELECT ORIGINAL_LOGIN()
SELECT SYSTEM_USER
```


