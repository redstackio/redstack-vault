---
id: d0ec0703-b77a-45e3-bc11-ea5a5c367bc7
name: Retrieve server principals with sysadmin role
type: command
executor: bash
data: SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER
  ('sysadmin',name) = 1
output: null
created_at: '2023-04-06T03:56:20.900610+00:00'
updated_at: '2023-04-10T20:36:42.521315+00:00'
---

# Retrieve server principals with sysadmin role

```bash
SELECT name,type_desc,is_disabled FROM sys.server_principals WHERE IS_SRVROLEMEMBER ('sysadmin',name) = 1
```
