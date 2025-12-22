---
type: command
executor: sql
data: 'select * from fn_my_permissions(null, ''server'');'
output: null
created_at: '2023-04-06T03:56:20.954736+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - permissions
  - discovery
verified: true
validated: true
---

# Retrieve-MSSQL-Server-Permissions

## Command

```sql
select * from fn_my_permissions(null, 'server');
```

## Description

This SQL command queries the MSSQL Server to list all effective permissions for the current user at the server level. It is used during discovery phases to assess access rights without requiring additional tools.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| null | Specifies the current user as the principal (no substitution needed) | Yes |
| 'server' | Targets server-level securables (fixed value) | Yes |

## Examples

### Basic Usage

Execute directly in a SQL client after connecting to the instance:

```sql
select * from fn_my_permissions(null, 'server');
```

### With Output Export (if supported)

```sql
select * from fn_my_permissions(null, 'server') INTO OUTFILE '/path/permissions.txt';
```

## Expected Output

A table of permissions, for example:

entity_name          | subentity_name | permission_state | permission_state_value
---------------------|----------------|------------------|-----------------------
CONTROL SERVER       | NULL           | GRANT            | 1
CREATE ANY DATABASE  | NULL           | GRANT            | 1
ALTER ANY LOGIN      | NULL           | DENY             | 0

Success is indicated by rows showing GRANT states for key permissions like CONTROL SERVER, confirming administrative access.

## Related

- [[procedures/Enumerate-MSSQL-Server-Permissions]]
- [[techniques/Permission-Groups-Discovery|T1069]]
