---
id: 40a0efa9-c4d3-46af-8860-351ac3bd422e
type: code
name: MSSQL-Enable-xp-cmdshell
language: sql
verified: true
created_at: '2023-04-06T03:56:33.953210+00:00'
updated_at: '2023-04-10T20:22:46.088423+00:00'
platforms:
  - Windows
tags:
  - mssql
  - configuration
validated: true
---

# MSSQL-Enable-xp-cmdshell

## Code

```sql
EXEC sp_configure 'show advanced options',1;
RECONFIGURE;
EXEC sp_configure 'xp_cmdshell',1;
RECONFIGURE;
```

## Description

SQL configuration script to enable the xp_cmdshell extended stored procedure, which is disabled by default in modern SQL Server versions for security.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Fixed configuration options | N/A |

## Usage

Run as sysadmin in an MSSQL session to activate OS command execution capabilities. Often injected via SQLi in exploitation chains.

## Detection

- SQL Server error logs or audit for sp_configure changes.
- Configuration queries like SELECT * FROM sys.configurations WHERE name = 'xp_cmdshell' showing value=1.

## Related

- [[procedures/MSSQL-Command-Execution-via-xp-cmdshell]]
