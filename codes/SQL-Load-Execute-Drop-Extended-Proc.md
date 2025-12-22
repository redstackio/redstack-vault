---
type: code
language: sql
verified: true
tags:
  - mssql
  - extended-proc
  - dll-load
platforms:
  - Windows
validated: true
---

# SQL-Load-Execute-Drop-Extended-Proc

## Code

```sql
-- can also be loaded from UNC path or Webdav
sp_addextendedproc 'xp_calc', 'C:\mydll\xp_calc.dll'
EXEC xp_calc
sp_dropextendedproc 'xp_calc'
```

## Description

This SQL code snippet demonstrates the full lifecycle of loading a custom DLL as an extended stored procedure in Microsoft SQL Server: adding it to the system, executing its function, and dropping it for cleanup. It runs the DLL code within the SQL Server process, enabling evasion of security controls by masquerading as database functionality. The comment notes flexibility in DLL sourcing from network locations to avoid local file drops.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'xp_calc' | Name of the extended procedure | 'xp_shell' |
| 'C:\mydll\xp_calc.dll' | Path to the DLL file | '\\server\share\mal.dll' |

## Usage

Execute this sequence in a SQL Server session with sysadmin privileges, such as via sqlcmd or SSMS. First, ensure the DLL is in place or accessible. This is typically used in post-exploitation for persistence or code execution on database servers. Integrate into larger attack chains for SQL Server compromise, delivering the DLL via initial access vectors like phishing or UNC paths.

## Detection

- Audit SQL Server logs for sp_addextendedproc, EXEC xp_*, and sp_dropextendedproc calls.
- Monitor sys.extended_procedures table changes and unusual DLL loads in process memory.
- Network monitoring for UNC/WebDAV access to suspicious shares during loads.
- Behavioral analysis: SQL Server process spawning child processes or outbound connections.

## Related

- [[procedures/Load-DLL-Using-sp_addextendedproc]]
