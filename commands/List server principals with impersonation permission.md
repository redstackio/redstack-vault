---
id: 6ed79db7-f91e-48aa-b484-271980b59757
name: List server principals with impersonation permission
type: command
executor: bash
data: 'select distinct b.name

  from sys.server_permissions a

  inner join sys.server_principals b

  on a.grantor_principal_id = b.principal_id

  where a.permission_name = ''impersonate'''
output: null
created_at: '2023-04-06T03:56:21.008928+00:00'
updated_at: '2023-04-10T20:36:39.959103+00:00'
---

# List server principals with impersonation permission

```bash
select distinct b.name
from sys.server_permissions a
inner join sys.server_principals b
on a.grantor_principal_id = b.principal_id
where a.permission_name = 'impersonate'
```


