---
id: abb2ca03-a454-41a9-b02e-b089e3ff3b36
name: Get Current User and Role
type: command
executor: bash
data: 'select suser_sname()

  Select system_user

  select is_srvrolemember(''sysadmin'')'
output: null
created_at: '2023-04-06T03:56:20.717419+00:00'
updated_at: '2023-04-10T20:36:36.496828+00:00'
---

# Get Current User and Role

```bash
select suser_sname()
Select system_user
select is_srvrolemember('sysadmin')
```


