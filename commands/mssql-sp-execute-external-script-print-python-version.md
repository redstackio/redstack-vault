---
id: b653b33e-1a80-4892-934e-2939d8205330
name: mssql-sp-execute-external-script-print-python-version
type: command
executor: sql
data: >-
  EXEC sp_execute_external_script @language = N'Python', @script = N'import sys;
  print(sys.version)';
output: null
created_at: '2023-04-06T03:56:33.953882+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
platforms:
  - Windows
tags:
  - mssql
  - python-execution
  - recon
verified: true
validated: true
---

# mssql-sp-execute-external-script-print-python-version

## Command

```sql
EXEC sp_execute_external_script @language = N'Python', @script = N'import sys; print(sys.version)';
```

## Description

Prints the Python version available in SQL Server's external scripting runtime.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @script | Python import and print statement | Yes |

## Examples

### Basic Usage

Run to verify Python support.

## Expected Output

Version string:

```
3.7.3 (default, Jun 27 2019, 00:00:00) [MSC v.1916 64 bit (AMD64)]
```

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
