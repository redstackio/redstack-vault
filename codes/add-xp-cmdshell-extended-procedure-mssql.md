---
id: 30e607b4-1ede-463e-b01b-e24d4d3bf1ca
name: add-xp-cmdshell-extended-procedure-mssql
type: code
language: sql
verified: true
created_at: '2023-04-06T03:56:20.266737+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - SQL Server
tags:
  - mssql
  - xp-cmdshell
  - extended-procedure
validated: true
---

# add-xp-cmdshell-extended-procedure-mssql

## Code

```sql
sp_addextendedproc 'xp_cmdshell','xplog70.dll'
```

## Description

This SQL code adds the xp_cmdshell extended stored procedure to the master database in SQL Server by registering the xplog70.dll library. It is used when the procedure has been dropped or removed for security hardening, restoring the ability to execute OS commands via T-SQL. This facilitates command execution in environments where standard enabling fails due to procedure absence.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 'xplog70.dll' | Path to the DLL file (hardcoded; adjust if custom location) | 'C:\Path\To\xplog70.dll' |

## Usage

Run in the master database context with sysadmin privileges after verifying the DLL exists in the SQL bin directory. Follow with granting EXECUTE permissions and enabling via sp_configure. This is a recovery step in advanced persistence or if defenders have removed the procedure.

## Detection

- SQL error logs or audits showing sp_addextendedproc calls.
- File integrity monitoring on SQL bin directories for DLL access/modification.
- Privilege escalation alerts for sysadmin users adding extended procedures.
- Behavioral analytics detecting unusual DLL loads by sqlservr.exe.

## Related

- [[procedures/Command-Execution-via-xp-cmdshell-MSSQL-Server]]
- [[commands/enable-xp-cmdshell-mssql]]
