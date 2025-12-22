---
id: 3c101383-366c-4771-a299-d56ec2c7b922
name: mssql-check-database-permissions
type: command
executor: sql
data: 'SELECT * FROM fn_my_permissions (NULL, ''DATABASE'');'
output: null
created_at: '2023-04-06T03:56:34.157829+00:00'
updated_at: '2023-04-10T20:22:47.331484+00:00'
platforms:
  - MSSQL
tags:
  - discovery
  - permissions
verified: true
validated: true
---

# mssql-check-database-permissions

## Command

```sql
SELECT * FROM fn_my_permissions (NULL, 'DATABASE');
```

## Description

This SQL command lists all effective permissions for the current user within the current database in MSSQL. It is useful for identifying data access rights, such as SELECT on tables, after exploiting a SQL injection vulnerability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| NULL | Targets the entire current database | Yes |
| 'DATABASE' | Specifies database-level scope | Yes |

## Examples

### Basic Usage

```sql
SELECT * FROM fn_my_permissions (NULL, 'DATABASE');
```

### Advanced Usage

To check permissions on a specific schema:

```sql
SELECT * FROM fn_my_permissions(NULL, 'DATABASE') WHERE subentity_name = 'dbo';
```

## Expected Output

Result set including permission_name (e.g., 'SELECT'), subentity_name, and class_desc ('DATABASE'). Example:

| entity_name | subentity_name | permission_name | permission_state | class_desc |
|-------------|----------------|-----------------|------------------|------------|
| NULL | NULL | SELECT | GRANT | DATABASE |

Look for broad grants like 'CONTROL' indicating database ownership.

## Related

- [[procedures/mssql-injection-list-permissions]]
- [[commands/mssql-check-server-permissions]]
