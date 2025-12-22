---
type: command
executor: sql
data: >-
  CREATE ASSEMBLY my_assembly FROM 'c:\temp\cmd_exec.dll' WITH PERMISSION_SET =
  UNSAFE; GO
output: null
created_at: '2023-04-06T03:56:20.431422+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
platforms:
  - SQL Server
tags:
  - assembly
  - clr
verified: true
validated: true
---

# sql-create-assembly-from-dll

## Command

```sql
CREATE ASSEMBLY $_ASSEMBLY_NAME
FROM '$_DLL_PATH'
WITH PERMISSION_SET = $_PERMISSION_SET;
GO
```

## Description

Imports a .NET DLL as a CLR assembly into SQL Server, enabling its use in stored procedures. UNSAFE permission allows full access including OS execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ASSEMBLY_NAME | Name for the assembly (e.g., my_assembly) | Yes |
| $_DLL_PATH | Full path to the DLL file (e.g., c:\temp\cmd_exec.dll) | Yes |
| $_PERMISSION_SET | Security level: SAFE, EXTERNAL_ACCESS, or UNSAFE | Yes |

## Examples

### Basic Usage

```sql
CREATE ASSEMBLY my_assembly
FROM 'c:\temp\cmd_exec.dll'
WITH PERMISSION_SET = UNSAFE;
GO
```

### Safe Permission

```sql
CREATE ASSEMBLY safe_assembly
FROM 'c:\temp\safe.dll'
WITH PERMISSION_SET = SAFE;
GO
```

## Expected Output

The module 'cmd_exec.dll' was successfully loaded into the assembly.

## Related

- [[procedures/Creating-and-Importing-CLR-Assembly-for-OS-Command-Execution-in-MSSQL]]
