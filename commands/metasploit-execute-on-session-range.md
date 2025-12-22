---
id: e06f7c96-5d95-43c4-b9fb-d814701ad981
name: metasploit-execute-on-session-range
type: command
executor: msfconsole
data: sessions -i $_SESSION_RANGE -c "$_COMMAND"
output: null
created_at: '2023-04-06T03:56:21.201764+00:00'
updated_at: '2023-04-10T20:24:56.124111+00:00'
platforms:
  - Linux
  - Windows
tags:
  - metasploit
  - sessions
verified: true
validated: true
---

# metasploit-execute-on-session-range

## Command

```msfconsole
sessions -i $_SESSION_RANGE -c "$_COMMAND"
```

## Description

Runs a command on a specified range of session IDs for targeted execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Interact/range flag | Yes |
| $_SESSION_RANGE | Range of IDs (e.g., 10-20) | Yes |
| -c | Command flag | Yes |
| $_COMMAND | Command to execute (e.g., 'id') | Yes |

## Examples

### Basic Usage

Execute 'id' on sessions 10-20.

```msfconsole
msf6 > sessions -i 10-20 -c "id"
[*] Command shell session 10: uid=0(root)
[*] Command shell session 11: uid=1000(user)
```

### Advanced Usage

Limit to specific compromised hosts.

## Expected Output

Output from each session in the range, labeled by ID.

## Related

- [[commands/metasploit-execute-on-multiple-sessions]]
- [[procedures/Session-Management-with-Metasploit]]
