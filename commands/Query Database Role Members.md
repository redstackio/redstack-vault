---
id: 26f88cf1-8d22-4801-9435-844ea4f73e99
name: Query Database Role Members
type: command
executor: bash
data: 'SELECT DB1.name AS DatabaseRoleName,

  isnull (DB2.name, ''No members'') AS DatabaseUserName

  FROM sys.database_role_members AS DRM

  RIGHT OUTER JOIN sys.database_principals AS DB1

  ON DRM.role_principal_id = DB1.principal_id

  LEFT OUTER JOIN sys.database_principals AS DB2

  ON DRM.member_principal_id = DB2.principal_id

  WHERE DB1.type = ''R''

  ORDER BY DB1.name;'
output: null
created_at: '2023-04-06T03:56:20.923585+00:00'
updated_at: '2023-04-10T20:36:30.386370+00:00'
---

# Query Database Role Members

```bash
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


