---
id: 807f7ff8-b267-4114-8b19-0d9150f41ea1
name: mssql-select-database-names
type: command
executor: sql
data: select name from master..sysdatabases
output: null
created_at: '2023-04-06T03:56:20.818969+00:00'
updated_at: '2023-04-10T20:36:33.201198+00:00'
platforms:
  - MSSQL
tags:
  - discovery
  - mssql
verified: true
validated: true
---

# mssql-select-database-names

## Command

```sql
select name from master..sysdatabases
```

## Description

This SQL command queries the sysdatabases system view in the master database to retrieve the names of all databases on the MSSQL instance. It is used during reconnaissance to map available databases without requiring elevated privileges, helping identify targets for further enumeration or data exfiltration.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| name | The column specifying the database name (fixed in query) | Yes |
| master..sysdatabases | System view path (master database, sys schema, sysdatabases view) | Yes |

No user-supplied parameters; the query is fixed for broad enumeration.

## Examples

### Basic Usage

Execute directly in a SQL client after connecting:

```sql
select name from master..sysdatabases;
GO
```

### Usage with Output Redirection (in sqlcmd)

```bash
sqlcmd -S server -U user -P pass -Q "select name from master..sysdatabases" -o dbs.txt
```

## Expected Output

A result set listing database names, typically in a tabular format:

name
----
master
model
msdb
tempdb
AdventureWorks  (example user DB)

Success is indicated by a complete list without errors. Common system databases include master, tempdb, model, and msdb; user databases vary by environment.

## Related

- [[procedures/Enumerate-MSSQL-Databases]] (procedure that uses this command)
- [[techniques/System Information Discovery|T1082]] (MITRE technique)
