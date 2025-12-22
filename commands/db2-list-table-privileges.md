---
id: fbcdd102-722a-4775-b221-167f81617509
name: db2-list-table-privileges
type: command
executor: sql
data: select * from syscat.tabauth
output: null
created_at: '2023-04-06T03:56:32.652959+00:00'
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

# db2-list-table-privileges

## Command

```sql
select * from syscat.tabauth;
```

## Description

This command queries the DB2 system catalog to list all privileges granted on tables, including grantee, schema, table name, and privilege types like SELECT, INSERT, or CONTROL. Use it during reconnaissance to identify accessible data objects and over-privileged users.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; queries all table authorizations. | No |

## Examples

### Basic Usage

```sql
select * from syscat.tabauth;
```

### Filtered Usage (Manual)

To filter for a specific schema, wrap in a client tool:
```sql
select * from syscat.tabauth where tabschema = 'MYSCHEMA';
```

## Expected Output

A table with columns such as:

GRANTEE | TABSCHEMA | TABNAME | SELECTAUTH | INSERTAUTH | ...
--------|-----------|---------|------------|------------| ----
PUBLIC  | SYSCAT    | COLUMNAUTH | Y          | N          | ...
USER1   | APP       | SENSITABLE | Y          | Y          | ...

Success is indicated by rows returned without authorization errors.

## Related

- [[procedures/Enumerate-DB2-User-Privileges]]
- [[commands/db2-show-current-user-table-privileges]]
