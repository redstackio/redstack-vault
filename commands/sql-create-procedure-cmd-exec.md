---
type: command
executor: sql
data: >-
  CREATE PROCEDURE [dbo].[cmd_exec] @execCommand NVARCHAR (4000) AS EXTERNAL
  NAME [my_assembly].[StoredProcedures].[cmd_exec]; GO
output: null
created_at: '2023-04-06T03:56:20.431422+00:00'
updated_at: '2023-04-10T20:36:42.151890+00:00'
platforms:
  - SQL Server
tags:
  - stored-procedure
  - clr
verified: true
validated: true
---

# sql-create-procedure-cmd-exec

## Command

```sql
CREATE PROCEDURE [dbo].[$_PROCEDURE_NAME] @execCommand NVARCHAR(4000)
AS EXTERNAL NAME [$_ASSEMBLY_NAME].[$_NAMESPACE].[$_METHOD_NAME];
GO
```

## Description

Creates a stored procedure that invokes a method from a loaded CLR assembly, allowing parameterized OS command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PROCEDURE_NAME | Name of the stored procedure (e.g., cmd_exec) | Yes |
| @execCommand | Input parameter for the command string (NVARCHAR(4000)) | Yes |
| $_ASSEMBLY_NAME | Loaded assembly name | Yes |
| $_NAMESPACE | .NET namespace in the assembly (e.g., StoredProcedures) | Yes |
| $_METHOD_NAME | Method name to call (e.g., cmd_exec) | Yes |

## Examples

### Basic Usage

```sql
CREATE PROCEDURE [dbo].[cmd_exec] @execCommand NVARCHAR(4000)
AS EXTERNAL NAME [my_assembly].[StoredProcedures].[cmd_exec];
GO
```

## Expected Output

The procedure 'cmd_exec' was created successfully.

## Related

- [[procedures/Creating-and-Importing-CLR-Assembly-for-OS-Command-Execution-in-MSSQL]]
