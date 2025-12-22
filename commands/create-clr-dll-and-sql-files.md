---
id: b272054f-56e0-45aa-8b66-3e2788f7204e
name: create-clr-dll-and-sql-files
type: command
executor: powershell
data: >-
  Create-SQLFileCLRDll -ProcedureName "runcmd" -OutFile runcmd -OutDir
  C:\Users\user\Desktop
output: null
created_at: '2023-04-06T03:56:20.364364+00:00'
updated_at: '2023-04-10T20:36:39.601743+00:00'
platforms:
  - Windows
tags:
  - clr
  - mssql
  - assembly
verified: true
validated: true
---

# create-clr-dll-and-sql-files

## Command

```powershell
Create-SQLFileCLRDll -ProcedureName "runcmd" -OutFile runcmd -OutDir C:\Users\user\Desktop
```

## Description

This PowerShell command generates C# source code for a CLR assembly DLL that executes OS commands, compiles it into a DLL, and creates a SQL script with the DLL content as a hexadecimal string for loading into MSSQL. Use this as the first step in CLR-based command execution procedures.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -ProcedureName | Name of the stored procedure to create in the assembly (e.g., "runcmd") | Yes |
| -OutFile | Base filename for output files (e.g., "runcmd" produces runcmd.cs, runcmd.dll, runcmd.sql) | Yes |
| -OutDir | Directory to save the generated files (e.g., C:\Users\user\Desktop) | Yes |

## Examples

### Basic Usage

```powershell
Create-SQLFileCLRDll -ProcedureName "runcmd" -OutFile runcmd -OutDir C:\Users\user\Desktop
```

### Advanced Usage

```powershell
Create-SQLFileCLRDll -ProcedureName "execshell" -OutFile shell -OutDir C:\temp
```

## Expected Output

No console output; success is indicated by the creation of three files in the specified directory:
- runcmd.cs: C# code defining a stored procedure that runs commands via Process.Start.
- runcmd.dll: Compiled .NET assembly.
- runcmd.sql: SQL script with CREATE ASSEMBLY FROM 0x[hex data]; CREATE PROCEDURE runcmd(@cmd nvarchar(4000)) AS EXTERNAL NAME...

If compilation fails, an error like "CSxxxx" will appear.

## Related

- [[procedures/mssql-clr-assembly-command-execution]]
- [[commands/invoke-clr-command-execution-whoami]]
