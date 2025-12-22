---
type: command
executor: powershell
data: winrm quickconfig
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - winrm
  - setup
verified: true
validated: true
---

# winrm-quickconfig

## Command

```powershell
winrm quickconfig
```

## Description

Initializes the WinRM service by enabling it, setting it to automatic startup, creating an HTTP listener on port 5985, and configuring the firewall rule. Run as administrator.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; interactive prompts for confirmation | No |

## Examples

### Basic Usage

```powershell
winrm quickconfig
```

> Prompts: "WinRM already set up?" or enables if not.

### Advanced Usage

Run non-interactively in scripts (not recommended for security):

```powershell
winrm quickconfig -quiet
```

## Expected Output

WinRM is set up for remote management.
Created a WinRM listener on HTTP://* to accept WS-Man requests to any IP on this machine.
WinRM firewall exception enabled.

## Related

- [[procedures/windows-remoting-via-winrm]]
- [[commands/winrm-enumerate-listeners]]
