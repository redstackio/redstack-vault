---
type: command
executor: powershell
data: winrm enumerate winrm/config/listener
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - config
verified: true
validated: true
---

# winrm-enumerate-listeners

## Command

```powershell
winrm enumerate winrm/config/listener
```

## Description

Lists all configured WinRM listeners, including addresses, ports, and enabled status, to verify service availability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Enumerates all listeners | No |

## Examples

### Basic Usage

```powershell
winrm enumerate winrm/config/listener
```

## Expected Output

Listener
    Address = HTTP://*
    Transport = HTTP
    Port = 5985
    Enabled = true
    ...

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-quickconfig]]
