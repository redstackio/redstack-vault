---
id: 014fc421-7aa5-4cb8-87a1-48b537251f88
name: mssql-check-recovery-model
type: command
executor: sql
data: >-
  USE master

  GO

  SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] =
  'database_name'
output: null
created_at: '2023-04-06T03:56:33.914847+00:00'
updated_at: '2023-04-10T20:22:42.032361+00:00'
platforms:
  - Windows
tags:
  - mssql
  - discovery
verified: true
validated: true
---

# mssql-check-recovery-model

## Command

```sql
USE master
GO
SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] = 'database_name'
```

## Description

This command queries the sys.databases system view to determine the current recovery model of a specified MSSQL database, which is essential before performing bulk operations like file reads via OpenRowset.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| database_name | Name of the target database to check | Yes |

## Examples

### Basic Usage

```sql
USE master
GO
SELECT [name], [recovery_model_desc] FROM sys.databases WHERE [name] = 'MyDB'
```

### Advanced Usage

To check all databases:

```sql
USE master
GO
SELECT [name], [recovery_model_desc] FROM sys.databases
```

## Expected Output

name    recovery_model_desc
MyDB    FULL

This shows the recovery model (e.g., FULL, BULK_LOGGED, SIMPLE). If FULL, bulk operations may fail.

## Related

- [[procedures/MSSQL-Read-File-via-INI-Disclosure]]
- [[commands/mssql-switch-to-bulk-logged-recovery]]
