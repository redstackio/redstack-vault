---
id: 8a286849-134d-4439-9086-ae268470d03c
name: metasploit-list-sessions
type: command
executor: msfconsole
data: sessions
output: null
created_at: '2023-04-06T03:56:21.201468+00:00'
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

# metasploit-list-sessions

## Command

```msfconsole
sessions
```

## Description

Lists all active Metasploit sessions, showing IDs, types, and target details for management.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Displays all sessions | No |

## Examples

### Basic Usage

Run to view current sessions.

```msfconsole
msf6 > sessions
Id  Type                   Information                  Connection
=   ====                   ===========                  ==========
1   shell windows/shell    192.168.1.100:4444 ->        192.168.1.50:12345
```

### Advanced Usage

Use 'sessions -l' for a detailed list.

## Expected Output

A table of sessions with columns for ID, type, info, and connection details.

## Related

- [[commands/metasploit-interact-with-session]]
- [[procedures/Session-Management-with-Metasploit]]
