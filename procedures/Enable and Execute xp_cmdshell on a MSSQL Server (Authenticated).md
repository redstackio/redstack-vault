---
id: 3e23abd5-38e8-4c79-817d-11a8544213af
name: Enable and Execute xp_cmdshell on a MSSQL Server (Authenticated)
type: procedure
verified: false
submitted: false
created_at: '2020-07-07T00:44:44.667549+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
platforms:
- Windows
commands:
- '[[MSSQL Enable xp_cmdshell]]'
- '[[xp_cmdshell Execute a Shell Command as the MSSQL User]]'
---

# Enable and Execute xp_cmdshell on a MSSQL Server (Authenticated)

## Summary

xp_cmdshell is a Microsoft SQL Server command which executes a string using a standard cmd.exe shell. This is often disabled on newer versions of MSSQL, but can be enabled with the "sp_configure" command. xp_cmdshell usually requires elevated database privileges, such as the "sa" account. 

## Description

# Description

xp_cmdshell is a Microsoft SQL Server command which executes a string using a standard cmd.exe shell. This is often disabled on newer versions of MSSQL, but can be enabled with the "sp_configure" command. xp_cmdshell usually requires elevated database privileges, such as the "sa" account.

# Instructions

1. Enable xp_cmdshell from an authorized session.

**Command** ([[MSSQL Enable xp_cmdshell]]):

```bash
EXEC sp_configure 'show advanced options', 1
go
RECONFIGURE
go
EXEC sp_configure 'xp_cmdshell', 1
go
RECONFIGURE
go
```

Note: Some mssql clients (eg: Impacket's mssqclient.py), do not require  "go" or "EXEC" for command execution. Consult the tool's documentation for any special syntax.

2. Execute commands with xp_cmdshell

**Command** ([[xp_cmdshell Execute a Shell Command as the MSSQL User]]):

```bash
EXEC xp_cmdshell "$_CMD"
go
```

## Platforms

- Windows

## Commands Used

- [[MSSQL Enable xp_cmdshell]]
- [[xp_cmdshell Execute a Shell Command as the MSSQL User]]
