---
id: ecdba2d9-7513-461a-b85c-8f38ed6b3237
name: metasploit-background-session
type: command
executor: msfconsole
data: CTRL+Z
output: null
created_at: '2023-04-06T03:56:21.201417+00:00'
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

# metasploit-background-session

## Command

```msfconsole
CTRL+Z
```

## Description

This keystroke backgrounds the currently active Metasploit session, returning control to the main msfconsole prompt without disconnecting the target.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| CTRL+Z | Keyboard shortcut to suspend session | Yes |

## Examples

### Basic Usage

While in an active session, press CTRL+Z to background it.

```msfconsole
[*] Session suspended
msf6 > 
```

### Advanced Usage

Use after entering a session to switch contexts quickly.

## Expected Output

The console returns to the msf6 > prompt, confirming the session is backgrounded and listed in 'sessions -l'.

## Related

- [[commands/metasploit-list-sessions]]
- [[procedures/Session-Management-with-Metasploit]]
