---
id: e2b2ee3c-7790-4c21-9d37-0df6ef365fe3
name: metasploit-background-current-session
type: command
executor: metasploit
data: bg
output: |-
  meterpreter > bg
  [*] Backgrounding session 1...
created_at: '2020-07-09T00:11:56.263753+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - session-management
verified: true
validated: true
---

# Metasploit Background Current Session

## Command

```metasploit
bg
```

## Description

This command backgrounds an active Meterpreter session in the Metasploit console, allowing the attacker to return to the main msfconsole prompt for loading modules or managing multiple sessions without terminating the connection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; applies to the current active session | No |

## Examples

### Basic Usage

```metasploit
bg
```

Used during an active session to suspend it temporarily.

### Advanced Usage

Background multiple sessions by interacting with each: `sessions -i 1` then `bg`, repeat for others.

## Expected Output

```
meterpreter > bg
[*] Backgrounding session 1...
msf6 >
```

The console returns to the msf prompt, and the session remains active in the background (check with `sessions -l`).

## Related

- [[commands/meterpreter-list-running-processes]]
- [[procedures/upgrade-windows-meterpreter-x32-to-x64]]
