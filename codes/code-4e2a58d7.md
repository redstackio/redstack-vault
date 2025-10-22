---
id: 4e2a58d7-8937-4748-a37d-3198b568e9dd
type: code
language: SQL
verified: false
created_at: '2023-04-06T03:56:20.923476+00:00'
updated_at: '2023-04-10T20:36:30.387083+00:00'
---

# Code Snippet 4e2a58d7

**Language**: SQL

```sql
SELECT DB1.name AS DatabaseRoleName,
isnull (DB2.name, 'No members') AS DatabaseUserName
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DB1
ON DRM.role_principal_id = DB1.principal_id
LEFT OUTER JOIN sys.database_principals AS DB2
ON DRM.member_principal_id = DB2.principal_id
WHERE DB1.type = 'R'
ORDER BY DB1.name;
```
