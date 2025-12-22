---
id: 7383b7da-43ab-42ae-a626-972a48bd7430
name: metasploit-interact-with-session
type: command
executor: msfconsole
data: sessions -i $_SESSION_ID
output: null
created_at: '2023-04-06T03:56:21.201587+00:00'
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

# metasploit-interact-with-session

## Command

```msfconsole
sessions -i $_SESSION_ID
```

## Description

Interacts with a specific session by ID, entering its shell or Meterpreter for direct command execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -i | Interact flag | Yes |
| $_SESSION_ID | Numeric session ID from 'sessions' list | Yes |

## Examples

### Basic Usage

Interact with session 1.

```msfconsole
msf6 > sessions -i 1
[*] Starting interaction with 1 ...
Meterpreter > 
```

### Advanced Usage

Switch back with CTRL+Z after interaction.

## Expected Output

Prompt changes to the session's interface (e.g., Meterpreter > or shell >).

## Related

- [[commands/metasploit-background-session]]
- [[procedures/Session-Management-with-Metasploit]]
