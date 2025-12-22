---
id: 295ae896-1841-4bd4-9034-093d04f9aa64
name: db2-show-current-user-database-privileges
type: command
executor: sql
data: select * from syscat.dbauth where grantee = current user
output: null
created_at: '2023-04-06T03:56:32.653063+00:00'
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

# db2-show-current-user-database-privileges

## Command

```sql
select * from syscat.dbauth where grantee = current user;
```

## Description

This command lists database authorities for the current DB2 user, such as CREATE_TAB or BINDADD, to evaluate capabilities for schema manipulation or binding procedures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| current user | Built-in function for the session user. | No |

## Examples

### Basic Usage

```sql
select * from syscat.dbauth where grantee = current user;
```

### For Specific User

```sql
select * from syscat.dbauth where grantee = 'OTHERUSER';
```

## Expected Output

Columns like GRANTEE, CREATETABAUTH, BINDADDAUTH:

GRANTEE | CREATETABAUTH | BINDADDAUTH
--------|---------------|-------------
USER1   | Y             | N

Indicates authorities granted to the user.

## Related

- [[procedures/Enumerate-DB2-User-Privileges]]
- [[commands/db2-show-current-user-table-privileges]]
