---
type: command
executor: powershell
data: 'Rubeus.exe klist [/luid:$_LUID]'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - discovery
verified: true
validated: true
---

# rubeus-klist

## Command

```powershell
Rubeus.exe klist [/luid:$_LUID]
```

## Description

Lists Kerberos tickets in the current session.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [/luid:$_LUID] | Specific LUID for session | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe klist
```

## Expected Output

Ticket list: "Service: krbtgt/EXAMPLE.COM, User: attacker@EXAMPLE.COM".

## Related

- [[tools/Rubeus]]
