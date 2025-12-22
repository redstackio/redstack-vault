---
id: cdd8f416-d08c-49c3-85f3-bf3474c5607f
name: mssql-check-server-permissions
type: command
executor: sql
data: 'SELECT * FROM fn_my_permissions(NULL, ''SERVER'');'
output: null
created_at: '2023-04-06T03:56:34.157655+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
platforms:
  - MSSQL
tags:
  - discovery
  - permissions
verified: true
validated: true
---

# mssql-check-server-permissions

## Command

```sql
SELECT * FROM fn_my_permissions(NULL, 'SERVER');
```

## Description

This SQL command queries the fn_my_permissions system function to retrieve all effective permissions granted to the current user at the server level in an MSSQL database. Use it during post-exploitation to assess administrative privileges after gaining query execution via SQL injection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| NULL | Specifies the entire server as the target object (no specific object name needed) | Yes |
| 'SERVER' | Indicates server-level permissions (use 'DATABASE' or 'OBJECT' for other scopes) | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM fn_my_permissions(NULL, 'SERVER');
```

### Advanced Usage

To filter results for specific permissions:

```sql
SELECT * FROM fn_my_permissions(NULL, 'SERVER') WHERE permission_name LIKE '%ADMIN%';
```

## Expected Output

A table with columns like entity_name, subentity_name, permission_name (e.g., 'CONTROL SERVER'), permission_state ('GRANT'), class_desc ('SERVER'), and principal_id. Example:

| entity_name | subentity_name | permission_name | permission_state | class_desc | principal_id |
|-------------|----------------|-----------------|------------------|------------|--------------|
| NULL | NULL | CONTROL SERVER | GRANT | SERVER | 1 |

If no high-privilege grants appear, the user has limited server access.

## Related

- [[procedures/mssql-injection-list-permissions]]
- [[commands/mssql-check-database-permissions]]
