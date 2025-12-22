---
id: 26f88cf1-8d22-4801-9435-844ea4f73e99
name: mssql-query-database-role-members
type: command
executor: sql
data: |-
  SELECT DB1.name AS DatabaseRoleName,
  isnull (DB2.name, 'No members') AS DatabaseUserName
  FROM sys.database_role_members AS DRM
  RIGHT OUTER JOIN sys.database_principals AS DB1
  ON DRM.role_principal_id = DB1.principal_id
  LEFT OUTER JOIN sys.database_principals AS DB2
  ON DRM.member_principal_id = DB2.principal_id
  WHERE DB1.type = 'R'
  ORDER BY DB1.name;
output: null
created_at: '2023-04-06T03:56:20.923585+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql
  - enumeration
  - query
verified: true
validated: true
---

# mssql-query-database-role-members

## Command

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

## Description

This SQL command queries the MSSQL system views to list all database roles and their user members. It is used during discovery phases to map database permissions and identify escalation opportunities. Execute it in a connected SQL session via SSMS, sqlcmd, or similar tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None (direct query) | The query has no user-supplied parameters; it runs against the current database context. | N/A |

## Examples

### Basic Usage

Execute directly in SSMS query window or via sqlcmd:

```bash
sqlcmd -S servername -U username -P password -Q "SELECT DB1.name AS DatabaseRoleName, isnull (DB2.name, 'No members') AS DatabaseUserName FROM sys.database_role_members AS DRM RIGHT OUTER JOIN sys.database_principals AS DB1 ON DRM.role_principal_id = DB1.principal_id LEFT OUTER JOIN sys.database_principals AS DB2 ON DRM.member_principal_id = DB2.principal_id WHERE DB1.type = 'R' ORDER BY DB1.name;"
```

### Advanced Usage

Filter for a specific role (e.g., db_owner):

```sql
SELECT DB1.name AS DatabaseRoleName,
isnull (DB2.name, 'No members') AS DatabaseUserName
FROM sys.database_role_members AS DRM
RIGHT OUTER JOIN sys.database_principals AS DB1
ON DRM.role_principal_id = DB1.principal_id
LEFT OUTER JOIN sys.database_principals AS DB2
ON DRM.member_principal_id = DB2.principal_id
WHERE DB1.type = 'R' AND DB1.name = 'db_owner'
ORDER BY DB1.name;
```

## Expected Output

A tabular result set showing roles and members:

DatabaseRoleName | DatabaseUserName
-----------------|-----------------
db_accessadmin   | user1

db_backupoperator| No members

public           | all_users

If successful, no errors like 'The SELECT permission was denied' appear, and all standard roles (e.g., db_owner, public) are listed.

## Related

- [[procedures/Enumerate-MSSQL-Database-Roles-and-User-Members]]
