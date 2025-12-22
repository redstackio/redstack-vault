---
id: 8794d72d-1b81-48ab-acc0-e107dffcfa80
name: metasploit-execute-on-multiple-sessions
type: command
executor: msfconsole
data: sessions -c "$_COMMAND"
output: null
created_at: '2023-04-06T03:56:21.201693+00:00'
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

# metasploit-execute-on-multiple-sessions

## Command

```msfconsole
sessions -c "$_COMMAND"
```

## Description

Executes a command across all active sessions, aggregating results for bulk operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c | Command execution flag | Yes |
| $_COMMAND | Shell command to run (e.g., 'whoami') | Yes |

## Examples

### Basic Usage

Run 'whoami' on all sessions.

```msfconsole
msf6 > sessions -c "whoami"
[*] Command shell session 1: user
[*] Command shell session 2: administrator
```

### Advanced Usage

Use for system info gathering.

## Expected Output

Per-session output prefixed with session ID.

## Related

- [[commands/metasploit-execute-on-session-range]]
- [[procedures/Session-Management-with-Metasploit]]
