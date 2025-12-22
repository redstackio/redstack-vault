---
id: 738899f5-4cc5-40d5-aba0-018acf7911fc
name: db2-show-current-user-table-privileges
type: command
executor: sql
data: select * from syscat.tabauth where grantee = current user
output: null
created_at: '2023-04-06T03:56:32.653023+00:00'
updated_at: '2023-04-10T20:22:04.113006+00:00'
platforms:
  - Linux
  - Windows
tags:
  - db2
  - enumeration
verified: true
validated: true
---

# db2-show-current-user-table-privileges

## Command

```sql
select * from syscat.tabauth where grantee = current user;
```

## Description

This command retrieves table-level privileges specifically for the currently connected DB2 user, showing access to schemas and tables. It helps assess the scope of current access for escalation planning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| current user | Built-in DB2 function returning the session user; no substitution needed. | No |

## Examples

### Basic Usage

```sql
select * from syscat.tabauth where grantee = current user;
```

### With Specific User (Manual Adjustment)

For another user:
```sql
select * from syscat.tabauth where grantee = 'OTHERUSER';
```

## Expected Output

Rows limited to the current user, e.g.:

GRANTEE | TABSCHEMA | TABNAME | SELECTAUTH
--------|-----------|---------|------------
USER1   | APP       | DATA    | Y

No rows indicate minimal table access.

## Related

- [[procedures/Enumerate-DB2-User-Privileges]]
- [[commands/db2-list-table-privileges]]
