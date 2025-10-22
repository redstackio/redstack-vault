---
id: f01d99dd-8c7c-48c7-a891-fa1f56142ef1
name: Add user to sysadmin role
type: command
executor: bash
data: EXEC master.dbo.sp_addsrvrolemember 'user', 'sysadmin';
output: null
created_at: '2023-04-06T03:56:34.073098+00:00'
updated_at: '2023-04-10T20:22:39.400786+00:00'
---

# Add user to sysadmin role

```bash
EXEC master.dbo.sp_addsrvrolemember 'user', 'sysadmin';
```
