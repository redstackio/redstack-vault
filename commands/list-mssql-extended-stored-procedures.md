---
id: 7461002f-725a-4f80-be4b-d4af2856ab3a
name: list-mssql-extended-stored-procedures
type: command
executor: powershell
data: Get-SQLStoredProcedureXP -Instance "$_INSTANCE" -Verbose
output: null
created_at: '2023-04-06T03:56:20.295541+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - enumeration
verified: true
validated: true
---

# list-mssql-extended-stored-procedures

## Command

```powershell
Get-SQLStoredProcedureXP -Instance "$_INSTANCE" -Verbose
```

## Description

This command queries an MSSQL instance to list all extended stored procedures, helping identify existing xp_* functions and potential injection points.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Instance ($__INSTANCE) | Target SQL Server instance in format SERVERNAME\INSTANCE (e.g., DBSERVERNAME\SQLEXPRESS) | Yes |
| -Verbose | Enables detailed output including procedure details | No |

## Examples

### Basic Usage

```powershell
Get-SQLStoredProcedureXP -Instance "DBSERVERNAME\SQLEXPRESS" -Verbose
```

### Advanced Usage

```powershell
Get-SQLStoredProcedureXP -Instance "DBSERVERNAME\SQLEXPRESS" | Select-Object Name, DllName
```

## Expected Output

A table or list of extended procedures, e.g.:

Name       : xp_cmdshell
DllName    : C:\Windows\System32\sqlserver.dll

Name       : xp_test
DllName    : \\10.10.0.1\temp\test.dll

## Related

- [[procedures/mssql-server-extended-stored-procedure-dll-injection]]
- [[tools/PowerUpSQL]]
